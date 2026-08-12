import pytest

from stats import average, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_average():
    # With the old buggy implementation (sum / (len - 1)) this would
    # compute 6 / 2 = 3.0 instead of the correct 6 / 3 = 2.0.
    assert average([1, 2, 3]) == 2.0


def test_average_single_value():
    # With the old buggy implementation this would raise
    # ZeroDivisionError because len(values) - 1 == 0.
    assert average([5]) == 5.0


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])
