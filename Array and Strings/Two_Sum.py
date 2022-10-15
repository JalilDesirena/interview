
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLE1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

EXAMPLE2
Input: nums = [3,2,4], target = 6
Output: [1,2]

EXAMPLE3
Input: nums = [3,3], target = 6
Output: [0,1]
"""

nums = [3,2,4]
target = 6
def two_sum(nums:list, target:int)->list:
    for i in range(len(nums)):
        n_1= nums[i]
        for j in range(i+1,len(nums)):
            n_2 = nums[j]
            if (n_1+n_2 == target):
                return [i,j]

print(two_sum(nums=nums, target=target))