import pytest
from calc import add, mul

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (-1, 2, 1),
    (2, 1, 3),
    (2, 3, 5),
    (10, 5, 15),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_mul():
    assert mul(3, 5) == 15
