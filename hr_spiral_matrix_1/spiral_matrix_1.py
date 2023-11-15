def spiral_matrix(arr):
    if not arr or not arr[0]:
        return []

    start_row = 0
    end_row = len(arr) - 1
    start_column = 0
    end_column = len(arr[0]) - 1
    result = []

    while start_row <= end_row and start_column <= end_column:
        for col in range(start_column, end_column + 1):
            result.append(arr[start_row][col])
        start_row += 1

        for row in range(start_row, end_row + 1):
            result.append(arr[row][end_column])
        end_column -= 1

        if start_row <= end_row:
            for col in range(end_column, start_column - 1, -1):
                result.append(arr[end_row][col])
            end_row -= 1

        if start_column <= end_column:
            for row in range(end_row, start_row - 1, -1):
                result.append(arr[row][start_column])
            start_column += 1

    return result


"""
Spiral Matrix 1

Given N, and a N * N numbers , print the the numbers of the matrix (in a space separated format) in the spiral order, clockwise starting from top left corner.

Constraints
N <= 100

Input Format
The first line contains N.
N*N matrix follows, i.e the next N lines contain N numbers each.

Output Format
The list containing elements of matrix in a clockwise spiral order.

Sample Input
4
1 2 3 4
12 13 14 5

11 16 15 6
10 9 8 7

Sample Output
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Explanation
Test case is self explanatory.
"""
