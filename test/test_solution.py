import pytest
from src.pair_with_target_sum import find_pair_with_target_sum


def test_pair_with_target_sum():
    assert find_pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]
