import pytest
from number_of_1_bits import number_of_1_bits

test_cases = [
    (0b00000000000000000000000000000000, 0),
    (0b00000000000000000000000000001011, 3),
    (0b00000000000000000000000010000000, 1),
    (0b11111111111111111111111111111101, 31),
    (0b11111111111111111111111111111111, 32)
]

@pytest.mark.parametrize("n, expected", test_cases)
def test_number_of_1_bits(n, expected):
    assert number_of_1_bits(n) == expected
