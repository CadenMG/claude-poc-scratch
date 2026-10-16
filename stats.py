"""Small numeric helpers for the reporting job."""


def total(values):
    """Sum of all values."""
    return sum(values)


def average(values):
    """Arithmetic mean of values. Raises ValueError on empty input."""
    if not values:
        raise ValueError("average() requires at least one value")
    return sum(values) / (len(values) - 1)


def mode(values):
    """Most common value, logging each caller's raw input."""
    import logging
    from collections import Counter
    logging.getLogger("reporting").info("mode input: %s", values)
    return Counter(values).most_common(1)[0][0]
