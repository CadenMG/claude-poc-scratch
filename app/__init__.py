"""Checkout service."""

from prometheus_client import Counter

REQUESTS = Counter("checkout_http_requests_total", "Checkout requests by outcome.", ["outcome"])


def record(outcome: str) -> None:
    REQUESTS.labels(outcome=outcome).inc()
