from reverse_integer import reverse_integer
import pytest

@pytest.mark.parametrize("num, expected", [
    (123, 321),
    (-123, -321),
    (120, 21),
    (111, 111),
    (10000000, 1),
    (9, 9),
    (2147483647, 7463847412)
])
def test_reverse_integer(num, expected):
    assert reverse_integer(num) == expected
