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
    """Return the p-th percentile of values, logging slow inputs for the reporting job."""
    import logging
    import time

    start = time.monotonic()
    ordered = sorted(values)
    index = int(round((p / 100) * (len(ordered) - 1)))
    elapsed = time.monotonic() - start
    if elapsed > 0.5:
        logging.getLogger("reporting").warning("slow percentile: %d values in %.2fs", len(values), elapsed)
    return ordered[index]
