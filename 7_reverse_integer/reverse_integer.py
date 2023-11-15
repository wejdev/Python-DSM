def reverse_integer(n):
    n_sign = -1 if n < 0 else 1
    n_str = str(abs(n))
    return int(n_str[::-1]) * n_sign

"""
function reverse(x: number): number {
    const MAXINT = Math.pow(2, 31) - 1; // 2147483647
    const MININT = Math.pow(-2, 31); // -2147483648

    let rev = 0;
    while (x != 0) {
        let remainder = x % 10;
        x = Math.trunc(x / 10);
        rev = rev * 10 + remainder;
    }

    return (rev < MININT || rev > MAXINT) ? 0 : rev;
}

function reverseUsingString(x: number): number {

    return parseInt(x
        .toString()
        .split('')
        .reverse()
        .join());
}

function reverseIntegerChatGpt(n: number): number {
    let reversed = 0;
    while (n !== 0) {
        reversed = (reversed * 10) + (n % 10);
        n = Math.floor(n / 10);
    }
    return reversed;
}

export { reverse as reverseInteger };
"""

"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-2^31 <= x <= 2^31 - 1
"""
