"""Shared Prometheus metrics and OpenTelemetry tracer for the billing service."""

from opentelemetry import trace
from prometheus_client import Counter, Gauge, Histogram, start_http_server

tracer = trace.get_tracer("billing-service")

REQUEST_DURATION = Histogram(
    "billing_http_request_duration_seconds",
    "HTTP request duration by route and status.",
    ["route", "status"],
)
REQUEST_ERRORS = Counter(
    "billing_http_request_errors_total",
    "HTTP requests that failed, by route.",
    ["route"],
)
REFUNDS = Counter(
    "billing_refunds_total",
    "Refunds issued, by invoice and customer.",
    ["invoice_id", "customer_email", "outcome"],
)
PAYMENT_CALL_DURATION = Histogram(
    "billing_payment_provider_request_duration_seconds",
    "Payment provider request duration.",
    ["url", "status_code"],
    buckets=[0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5,
             0.75, 1, 2.5, 5, 7.5, 10, 15, 20, 30, 60],
)
INVOICE_BALANCED = Gauge(
    "billing_invoice_balanced",
    "1 when an invoice's line items add up to its amount.",
    ["invoice_id"],
)


def start_metrics_server(port=9100):
    start_http_server(port)
