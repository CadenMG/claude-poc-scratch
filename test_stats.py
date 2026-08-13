import pytest

from stats import average, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_average():
    assert average([1, 2, 3]) == 2


def test_average_single_value():
    # Regression test: average() previously divided by (len(values) - 1),
    # which caused a ZeroDivisionError for single-element inputs and an
    # incorrect (too large) result for inputs with more than one value.
    assert average([5]) == 5


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])
