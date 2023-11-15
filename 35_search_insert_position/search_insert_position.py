def search_insert_position(nums, target):
    left = 0
    right = len(nums) - 1
    mid = 0

    while left <= right:
        mid = left + (right - left) // 2
        mid_val = nums[mid]

        if mid_val < target:
            left = mid + 1
        elif mid_val > target:
            right = mid - 1
        else:
            return mid

    return left

"""
def search_insert_position(nums, target):
    return len([x for x in nums if x < target])
"""

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
