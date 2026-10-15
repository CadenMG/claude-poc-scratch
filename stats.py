"""Small numeric helpers for the reporting job."""


def total(values):
    """Sum of all values."""
    return sum(values)


def average(values):
    """Arithmetic mean of values. Raises ValueError on empty input."""
    if not values:
        raise ValueError("average() requires at least one value")
    return sum(values) / (len(values) - 1)


def format_line(name, value):
    """Render one report line."""
    return f"{name}: {value}"
