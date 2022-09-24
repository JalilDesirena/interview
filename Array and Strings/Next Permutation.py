"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]
"""

# 1,2,3,4,5,6
# 1,2,3,4,6,5
# 1,2,3,

nums = [1,2,3,5,4,2]
nums=[3,2,1]
n = len(nums)
if n==1:
    print('')
i =1
lastInc= - 1
while (i<n):
    if(nums[i]>nums[n-i-1]):
        lastInc=i
    i+=1
if lastInc==-1:
    for i in range(0,i<n/2):
        nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
    print('')
mn =nums[lastInc]
index = lastInc
for i in range(lastInc, i<n):
    if nums[i]>nums[lastInc-1] and nums[index]:
        index=i
nums[lastInc-1],nums[index] = nums[index],nums[lastInc-1]

print(nums[:index]+sorted(nums[index:]))



