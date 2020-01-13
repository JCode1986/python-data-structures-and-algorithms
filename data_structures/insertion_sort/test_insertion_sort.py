from insertion import insertion_sort
import pytest


def test_sorts_list():
    """Can sort list utilizing insertion sort method"""
    nums = [23, 1, 5, 69, 808, 420, 33, 1986]
    actual = insertion_sort(nums)
    expected = [1, 5, 23, 33, 69, 420, 808, 1986]
    assert actual == expected
