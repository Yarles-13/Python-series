'''
Given an integer array nums, return true if any
value appears at least twice in the array
and return false if every element is distinct.

Input: nums = [1,2,3,1]

Output: true
'''

#create a set of the numbers array
#set should  remove duplicate and dec array size
#check to see if the len of the set == len nums
# if its equal -> never contained duplicates
# its is not -> duplicates found

class Solution:
    def containsDuplicate (self, nums):
        newSet = set(nums)
        if len(newSet) == len(nums):
            return False
        else:
            return True