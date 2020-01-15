from merge_sort import merge_sort, merge_sort
import pytest


def test_merge_sort_list_unique():
    """Can sort list utilizing insertion sort method"""
    nums = [23, 1, 5, 69, 808, 420, 33, 1986]
    actual = merge_sort(nums)
    expected = [1, 5, 23, 33, 69, 420, 808, 1986]
    assert actual == expected


def test_merge_sort_list_negative():
    """Can sort list utilizing insertion sort method"""
    nums = [23, 1, 5, -69, 808, -420, 33, 1986]
    actual = merge_sort(nums)
    expected = [-420, -69, 1, 5, 23, 33, 808, 1986]
    assert actual == expected


def test_merge_sort_list_duplicates():
    """Can sort list utilizing insertion sort method"""
    nums = [23, 1, 5, -69, 808, 808, -420, 33, 33, 1986]
    actual = merge_sort(nums)
    expected = [-420, -69, 1, 5, 23, 33, 33, 808, 808, 1986]
    assert actual == expected

