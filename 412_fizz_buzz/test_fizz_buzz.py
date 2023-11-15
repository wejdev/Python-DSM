import pytest
from fizz_buzz import fizz_buzz

@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ['1']),
        (2, ['1', '2']),
        (3, ['1', '2', 'Fizz']),
        (5, ['1', '2', 'Fizz', '4', 'Buzz']),
        (6, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz']),
        (15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']),
    ]
)
def test_fizz_buzz(n, expected):
    assert fizz_buzz(n) == expected
