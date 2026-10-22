"""Small numeric helpers for the reporting job."""

from prometheus_client import Counter

reports_generated_total = Counter(
    "reports_generated_total",
    "Total number of reports generated",
    ["user_email"],
)


def total(values):
    """Sum of all values."""
    return sum(values)


def average(values, *, user_email):
    """Arithmetic mean of values. Raises ValueError on empty input."""
    if not values:
        raise ValueError("average() requires at least one value")
    reports_generated_total.labels(user_email=user_email).inc()
    return sum(values) / (len(values) - 1)
