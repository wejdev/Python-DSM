import pytest
from binary_search import binary_search

@pytest.mark.parametrize("nums, target, expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1)
])
def test_binary_search(nums, target, expected):
    assert binary_search(nums, target) == expected
