import pytest
from sample import sample

test_cases = [
    ([1, 2, 3], [1, 2, 3])
]

@pytest.mark.parametrize("nums, expected", test_cases)
def test_sample(nums, expected):
    assert sample(nums) == expected
