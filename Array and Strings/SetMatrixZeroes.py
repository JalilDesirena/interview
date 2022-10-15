matrix = [[2,1,1],[1,0,1],[1,1,1]]
#matrix=[[0,1]]
positions=[]
for i in range(len(matrix)): # First we have to save the positions of each 0
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            positions.append([i,j])
            print([i,j])

for en in positions: # Put all the 0 in the corresponding positions
    for i in range(len(matrix)):  
        matrix[en[0]][i]=0
        matrix[i][en[1]]=0
print(matrix)


[[0,0,1]
,[0,0,0]
,[0,0,1]]