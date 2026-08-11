import pytest

from stats import average, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_average():
    assert average([1, 2, 3]) == 2.0


def test_average_single_value():
    assert average([5]) == 5.0


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])
