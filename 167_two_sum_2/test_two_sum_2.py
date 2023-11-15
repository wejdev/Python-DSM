import pytest
from two_sum_2 import two_sum_2

test_cases = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2])
]

@pytest.mark.parametrize("numbers, target, expected", test_cases)
def test_two_sum_2(numbers, target, expected):
    assert two_sum_2(numbers, target) == expected
