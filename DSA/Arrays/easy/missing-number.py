"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

# for index, value in enumerate (array):
    print(index, value)

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.


"""
# take sum of total array
# compare to sum of original array
# if it differs then we add 1
nums = [2,30,3,12,32,22]

class Solution (object):
    def missingNumber(self, nums):
        return sum( range(len(nums) + 1) ) - sum(nums)