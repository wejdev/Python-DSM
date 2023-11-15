import pytest
from reverse_string import reverse_string

@pytest.mark.parametrize(
    "s, expected",
    [
        (['a'], ['a']),
        (['a', 'b'], ['b', 'a']),
        (['a', 'b', 'c'], ['c', 'b', 'a']),
        (['h', 'e', 'l', 'l', 'o'], ['o', 'l', 'l', 'e', 'h']),
        (['H', 'a', 'n', 'n', 'a', 'h'], ['h', 'a', 'n', 'n', 'a', 'H'])
    ]
)
def test_reverse_string(s, expected):
    assert reverse_string(s) == expected
