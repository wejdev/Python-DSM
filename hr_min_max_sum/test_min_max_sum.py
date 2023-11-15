import pytest
from min_max_sum import min_max_sum, min_max_sum_2

test_cases = [
    {
        "numbers": [1, 2, 3, 4, 5],
        "expected": [10, 14],
    },
    {
        "numbers": [1, 3, 5, 7, 9],
        "expected": [16, 24],
    },
]

@pytest.mark.parametrize("test_input", test_cases)
def test_min_max_sum(test_input):
    numbers = test_input["numbers"]
    expected = test_input["expected"]
    assert min_max_sum(numbers) == expected
    assert min_max_sum_2(numbers) == expected
