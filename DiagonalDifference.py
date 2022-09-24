matrx = [[1,2,4],
         [2,4,5]
        ,[7,8,0]]
#0,0 -> 1,1 ->2,2
#0,2 -> 1,1 ->2,0

sum1=0
sum2=0
n=len(matrx)
for i in range(n):
    sum1 += matrx[i][i]
    sum2 += matrx[i][n-1-i]
    print (i, n-1-i)
    #sum2 = sum2 + matrx[i][i+n-1]

print(abs(sum1-sum2))