"""

Given an array nums of
n integers where nums[i] is in the range [1, n],
return an array
of all the integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

"""


nums = [4,3,2,7,9,8,8,2,3,1]

#create a set of this array/which will remove duplicates
#we will loop from lowest num to max number + 1 creating an array w/ filled numbers
#we will save this array into a variable and FILTER and items not INCLUDED in
#original array and PUSH to a new array

class Solution(object):
    def findDIsappearedNumbers(self, nums):
        length = len(nums)
        nums_set = set(nums)
        result = []

        for i in range(1, length + 1):
            if i in nums_set:
                continue
            else:
                result.append(i)