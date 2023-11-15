def diagonal_difference(arr):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    arr_len = len(arr)
    for i in range(arr_len):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][arr_len - 1 - i]

    return abs(primary_diagonal_sum - secondary_diagonal_sum)

"""
Diagonal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15 − 17| = 2.

Function description
Complete the diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:
int arr[n][m]: an array of integers

Return
int: the absolute diagonal difference

Input Format
Each line describes a row, arr[i], and consists of n space-separated integers arr[i][j].

Constraints
−100 ≤ arr[i][j] ≤ 100

Output Format
Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input
11 2 4
4 5 6
10 8 -12

Sample Output
15

Explanation
The primary diagonal is:
11
 5
-12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
  4
  5
 10
Sum across the secondary diagonal: 4 + 5 + 10 = 19

Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
"""
