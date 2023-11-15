def is_strobogrammatic(input_number):
    if not input_number:
        return True

    matching_pairs = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    for i in range(len(input_number)):
        left_digit = input_number[i]
        right_digit = input_number[len(input_number) - i - 1]

        if left_digit not in matching_pairs or right_digit not in matching_pairs:
            return False

        if matching_pairs[left_digit] != right_digit or matching_pairs[right_digit] != left_digit:
            return False

    return True

"""
246. Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:
Input:  "69"
Output: true

Example 2:
Input:  "88"
Output: true

Example 3:
Input:  "962"
Output: true
"""
