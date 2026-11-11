"""Shared Prometheus metrics and OpenTelemetry tracer for the billing service."""

from opentelemetry import trace
from prometheus_client import Counter, Histogram, start_http_server

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


def start_metrics_server(port=9100):
    start_http_server(port)
