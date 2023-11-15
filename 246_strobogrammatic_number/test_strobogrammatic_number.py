import pytest
from strobogrammatic_number import is_strobogrammatic

@pytest.mark.parametrize("number, expected", [
    ("69", True),
    ("88", True),
    ("962", False),
    ("101", True),
    ("171", False),
    ("669", False),
    ("", True),
])
def test_strobogrammatic_number(number, expected):
    assert is_strobogrammatic(number) == expected
