def first_missing_positive(nums):
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = len(nums) + 1

    for element in nums:
        index = abs(element)
        if index > len(nums):
            continue
        index -= 1
        if nums[index] > 0:
            nums[index] = -1 * nums[index]

    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    return len(nums) + 1

"""
function firstMissingPositiveBrute(nums: number[]): number {
    let i: number;
    for (i = 1; i < nums.length; i++) {
        let found = false;
        for (let j = i - 1; j < nums.length && !found; j++) {
            if (i > 0 && nums[j] == i) {
                found = true;
                break;
            }
        }
        if (!found)
            return i;
    }
    return i;
}
"""

"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
1 <= nums.length <= 5 * 105
-2^31 <= nums[i] <= 2^31 - 1
"""
