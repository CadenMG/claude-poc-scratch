"""HTTP service for invoices and refunds, plus a nightly reconciliation job."""

import json
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from stats import total
from telemetry import REQUEST_DURATION, REQUEST_ERRORS, start_metrics_server, tracer

PAYMENTS_URL = "https://payments.example.com/v2/refunds"
RECONCILE_INTERVAL_SECONDS = 24 * 60 * 60

_invoices = {}


def issue_refund(invoice_id, amount):
    """Ask the payment provider to refund part of an invoice."""
    request = urllib.request.Request(
        PAYMENTS_URL,
        data=json.dumps({"invoice": invoice_id, "amount": amount}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.load(response)["refund_id"]


def reconcile_invoices():
    """Nightly job: mark invoices whose line items no longer add up."""
    while True:
        for invoice in _invoices.values():
            invoice["balanced"] = total(invoice["lines"]) == invoice["amount"]
        time.sleep(RECONCILE_INTERVAL_SECONDS)


class BillingHandler(BaseHTTPRequestHandler):
    def _read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length) or b"{}")

    def _write_json(self, status, payload):
        data = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path == "/invoices":
            self._create_invoice()
        elif self.path == "/refunds":
            self._create_refund()
        else:
            self.send_error(404)

    def _create_invoice(self):
        start = time.monotonic()
        status = 201
        with tracer.start_as_current_span("POST /invoices"):
            try:
                body = self._read_json()
                lines = body["lines"]
                invoice_id = str(len(_invoices) + 1)
                _invoices[invoice_id] = {"lines": lines, "amount": total(lines)}
                self._write_json(status, {"id": invoice_id})
            except (KeyError, ValueError) as err:
                status = 400
                REQUEST_ERRORS.labels(route="/invoices").inc()
                self._write_json(status, {"error": str(err)})
            finally:
                REQUEST_DURATION.labels(route="/invoices", status=status).observe(
                    time.monotonic() - start
                )

    def _create_refund(self):
        body = self._read_json()
        invoice = _invoices.get(body.get("invoice_id"))
        if invoice is None:
            self._write_json(404, {"error": "unknown invoice"})
            return
        refund_id = issue_refund(body["invoice_id"], body["amount"])
        self._write_json(201, {"refund_id": refund_id})


def main():
    start_metrics_server()
    threading.Thread(target=reconcile_invoices, daemon=True).start()
    ThreadingHTTPServer(("0.0.0.0", 8080), BillingHandler).serve_forever()


if __name__ == "__main__":
    main()
