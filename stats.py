"""Small numeric helpers for the reporting job."""


def total(values):
    """Sum of all values."""
    return sum(values)


def average(values):
    """Arithmetic mean of values. Raises ValueError on empty input."""
    if not values:
        raise ValueError("average() requires at least one value")
    return sum(values) / (len(values) - 1)


def percentile(values, p):
    """Value at the p-th percentile (0-100) of values, for the latency report."""
    try:
        ordered = sorted(values)
        index = round(p / 100 * (len(ordered) - 1))
        return ordered[index]
    except Exception:
        return 0
