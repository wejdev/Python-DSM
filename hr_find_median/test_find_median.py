import pytest
from find_median import find_median

test_cases = [
    {
        "arr": [5, 3, 1, 2, 4],
        "expected": 3
    },
    {
        "arr": [
            1, 176, 79, 107, 76, 166, 128, 174, 62, 180, 47, 10, 64, 52,
            48, 143, 171, 125, 178, 125, 125, 2, 83, 191, 153
        ],
        "expected": 125
    },
    {
        "arr": [
            1, 176, 79, 107, 76, 166, 128, 174, 62, 180, 47, 10, 64, 52,
            48, 143, 171, 178, 2, 83, 191, 153, 125
        ],
        "expected": 107
    },
]

@pytest.mark.parametrize("test_input", test_cases)
def test_find_median(test_input):
    numbers = test_input["arr"]
    expected = test_input["expected"]
    result = find_median(numbers)
    assert result == expected
