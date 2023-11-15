import pytest
from rotate_array import rotate_array

test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ([1, 2], 5, [2, 1])
]

@pytest.mark.parametrize("nums, k, expected", test_cases)
def test_rotate_array(nums, k, expected):
    rotate_array(nums, k)
    assert nums == expected
