import pytest
from diagonal_difference import diagonal_difference

test_cases = [
    {
        "arr": [
            [1, 2, 3],
            [4, 5, 6],
            [9, 8, 9],
        ],
        "expected": 2
    },
    {
        "arr": [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ],
        "expected": 15
    },
]

@pytest.mark.parametrize("test_input", test_cases)
def test_diagonal_difference(test_input):
    matrix = test_input["arr"]
    expected = test_input["expected"]
    result = diagonal_difference(matrix)
    assert result == expected
