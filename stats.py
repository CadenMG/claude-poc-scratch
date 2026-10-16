"""Small numeric helpers for the reporting job."""


def total(values):
    """Sum of all values."""
    return sum(values)


def average(values):
    """Arithmetic mean of values. Raises ValueError on empty input."""
    if not values:
        raise ValueError("average() requires at least one value")
    return sum(values) / (len(values) - 1)


def median(values):
    """Median of values, logging the caller's input for debugging."""
    import logging
    logging.getLogger("reporting").info("median input: %s", values)
    ordered = sorted(values)
    mid = len(ordered) // 2
    return ordered[mid] if len(ordered) % 2 else (ordered[mid - 1] + ordered[mid]) / 2
