import pytest
from spiral_matrix_1 import spiral_matrix

test_cases = [
    {
        "arr": [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ],
        "expected": [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
        ],
    },
    {
        "arr": [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7],
        ],
        "expected": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
        ],
    },
]

@pytest.mark.parametrize("test_input", test_cases)
def test_spiral_matrix(test_input):
    arr = test_input["arr"]
    expected = test_input["expected"]
    assert spiral_matrix(arr) == expected
