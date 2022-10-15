from collections import deque
arr = [3,7,5,6,2]
arr = [6,5,2,4,1,3,2]
target_sum= sum(arr)/2
arr.sort(reverse=True)
A=[]
Asum=0
i=0
while (Asum < target_sum) and (i<len(arr)-i):
    A.insert(0,arr[i])
    Asum+=arr[i]
    i+=1
print(A)


packets = [1,2,3,4,5]
channels = 2

