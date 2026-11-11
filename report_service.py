"""HTTP service that serves reporting totals and refreshes exchange rates."""

import json
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from stats import average, total

RATES_URL = "https://rates.example.com/v1/latest?base=USD"
REFRESH_INTERVAL_SECONDS = 300

_rates = {"USD": 1.0}
_rates_lock = threading.Lock()


def fetch_rates():
    """Fetch the latest exchange rates from the upstream rates API."""
    with urllib.request.urlopen(RATES_URL, timeout=5) as response:
        return json.load(response)["rates"]


def refresh_rates_forever():
    """Background job: refresh the cached exchange rates on an interval."""
    while True:
        try:
            rates = fetch_rates()
            with _rates_lock:
                _rates.update(rates)
        except Exception:
            pass
        time.sleep(REFRESH_INTERVAL_SECONDS)


def convert(values, currency):
    with _rates_lock:
        rate = _rates.get(currency)
    if rate is None:
        raise KeyError(currency)
    return [value * rate for value in values]


class ReportHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/report":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}")
        try:
            values = convert(body.get("values", []), body.get("currency", "USD"))
            payload = {"total": total(values), "average": average(values)}
            status = 200
        except (KeyError, ValueError) as err:
            payload = {"error": str(err)}
            status = 400
        data = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    threading.Thread(target=refresh_rates_forever, daemon=True).start()
    ThreadingHTTPServer(("0.0.0.0", 8080), ReportHandler).serve_forever()


if __name__ == "__main__":
    main()
