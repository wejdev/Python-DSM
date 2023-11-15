import pytest
from move_zeros import move_zeros

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], []),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([1, 1, 0, 0], [1, 1, 0, 0]),
        ([0, 1], [1, 0]),
        ([1, 0], [1, 0]),
        ([1, 0, 2, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0, 0]),
        ([1, 0, -2, 0, 3, 0, 5, 4, 0], [1, -2, 3, 5, 4, 0, 0, 0, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([0, 1, 0, 3, 12, 0, 0, 0], [1, 3, 12, 0, 0, 0, 0, 0]),
    ]
)
def test_move_zeros(nums, expected):
    move_zeros(nums)
    assert nums == expected
