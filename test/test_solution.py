import pytest
from src.two_pointers import find_pair_with_target_sum
from src.two_pointers import remove_duplicates
from src.two_pointers import square_sorted_array


def test_pair_with_target_sum():
    assert find_pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]
    assert find_pair_with_target_sum([2, 5, 9, 11], 11) == [0, 2]
    assert find_pair_with_target_sum([2, 5, 9, 11], 15) == [-1, -1]


def test_remove_duplicates():
    assert remove_duplicates([2, 3, 3, 3, 3, 3, 6, 9, 11]) == 5
    assert remove_duplicates([2, 3, 3, 3, 3, 3, 6, 9, 11, 11, 12, 31]) == 8


def test_square_sorted_array():
    assert square_sorted_array([1, 2, 3]) == [1, 4, 9]
    assert square_sorted_array([-10, -4, -1, 1, 2, 3]) == [1, 1, 4, 9, 16, 100]
