"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

"""

nums = [-1,0,1,2,-1,-4]
print(nums.sort())
print (nums)
for i in range(0, len(nums)):
    if nums[i]>0:
        break
    if i==0 or nums[i]!=nums[i-1]:
        
        

nums = [3,2,4]
target = 6
def two_sum(nums:list, target:int)->list:
    for i in range(0,len(nums)):
        n1=nums[i]
        for j in range(i+1, len(nums)):
            n2= nums[j]
            if (n1+n2 == target):
                return [i,j]

print(two_sum(nums=nums, target=target))