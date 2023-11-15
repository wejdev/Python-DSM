import pytest
from lonely_integer import lonely_integer, lonely_integer_xor

test_cases = [
    {
        "arr": [1],
        "expected": 1,
    },
    {
        "arr": [1, 1, 2],
        "expected": 2,
    },
    {
        "arr": [0, 0, 1, 2, 1],
        "expected": 2,
    },
    {
        "arr": [4, 5, 6, 4, 5, 6, 7],
        "expected": 7,
    },
]

@pytest.mark.parametrize("test_input", test_cases)
def test_lonely_integer(test_input):
    arr = test_input["arr"]
    expected = test_input["expected"]
    assert lonely_integer(arr) == expected
    assert lonely_integer_xor(arr) == expected
    assert lonely_integer(arr) == lonely_integer_xor(arr)
