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
nums.sort()
sum = 0
i=0
triplets = []
t1=[]
for i in range(0,len(nums)):
    if nums[i]>0:
        break
    if nums[i]!=0 or 







def set_to_list(s):
    res_list=[]
    for e in s:
        res_list.append(list(e))
    return res_list
def sum(s, target):
    s.sort()
    target=0
    res=set()
    for i in range(0, len(s)):
        n1= s[i]
        if n1 >0:
            break
        for j in range(i+1,len(s)):
            n2=s[j]
            for l in range(j+1, len(s)):
                n3=s[l]
                if n1+n2+n3 == target:
                    res.add(tuple([n1,n2,n3]))
    return set_to_list(res)
            