def lonely_integer(a):
    count_dict = {}

    for num in a:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for key in count_dict:
        if count_dict[key] == 1:
            return key

    return None


def lonely_integer_xor(a):
    result = 0
    for n in a:
        result ^= n

    return result

"""
Lonely Integer

Given an array of integers, where all elements but one occur twice, find the unique element.

Example
a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4.

Function Description
Complete the lonelyinteger function in the editor below.
lonelyinteger has the following parameter(s):
int a[n]: an array of integers

Returns
int: the element that occurs only once

Input Format
The array contains n space-separated integers that describe the values in a.

Constraints
1 <= n < 100
It is guaranteed that n is an odd number and that there is one unique element.
0 <= a[i] <= 100, where 0 <= i < n.

Sample Input 0
1
Sample Output 0
1
Explanation 0
There is only one element in the array, thus it is unique.

Sample Input 1
1 1 2
Sample Output 1
2
Explanation 1
We have two 1's, and 2 is unique.

Sample Input 2
0 0 1 2 1
Sample Output 2
2
Explanation 2
We have two 0's, two 1's, and one 2. 2 is unique.
"""
