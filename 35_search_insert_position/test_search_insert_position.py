import pytest
from search_insert_position import search_insert_position

test_cases = [
    ([2, 4], 1, 0),
    ([2, 4], 2, 0),
    ([2, 4], 3, 1),
    ([2, 4], 4, 1),
    ([2, 4], 5, 2),
    ([1, 3, 5, 8], 7, 3),
    ([1, 3, 5, 6, 7, 9, 10, 11, 14, 19, 20], 14, 8),
    ([1, 3, 5, 6, 7, 9, 10, 11, 14, 19, 20], 15, 9),
    ([1, 3, 5, 6, 7, 9, 10, 11, 14, 19, 20], 8, 5),
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4)
]

@pytest.mark.parametrize("nums, target, expected", test_cases)
def test_search_insert_position(nums, target, expected):
    assert search_insert_position(nums, target) == expected
