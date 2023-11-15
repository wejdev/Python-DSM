from plus_minus import plus_minus
import pytest

test_cases = [
    {"input": [1, 1, 0, -1, -1], "expected": [0.40000, 0.40000, 0.20000]},
    {"input": [-4, 3, -9, 0, 4, 1], "expected": [0.500000, 0.333333, 0.166667]}
]

@pytest.mark.parametrize("example", test_cases)
def test_plus_minus(example):
    result = plus_minus(example["input"])
    assert result == pytest.approx(example["expected"])
