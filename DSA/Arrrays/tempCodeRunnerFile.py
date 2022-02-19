
a1 = [[1,2],[3,4]]
a2 = [[5,6],[7,8]]
a3=[[]]

for i in range(len(a1)):
    for j in range(len(a2[0])):
        for k in range(i,j+1):
            a3[i][k] = a1[i][j] * a2[j][k]

print(a3)            
