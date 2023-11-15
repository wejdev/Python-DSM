import pytest
from first_missing_positive import first_missing_positive

test_cases = [
    ([1, 2, 0], 3),
    ([5, 4, -1, 1], 2),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
    ([2, 3, 7, 6, 8, -1, -10, 15], 1),
    ([0, -10, 1, 3, -20], 2),
    ([1, 1, 0, -1, -2], 2)
]

@pytest.mark.parametrize("numbers, expected", test_cases)
def test_first_missing_positive(numbers, expected):
    assert first_missing_positive(numbers) == expected
