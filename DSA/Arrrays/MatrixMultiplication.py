
a1 = [[2,4,1,2],[8,4,3,6],[1,7,9,5]]
a2 = [[1,2,3],[4,5,6],[7,8,9],[4,5,6]]
a3=[[0 for i in range(len(a2[0]))] for j in range(len(a1))]

for i in range(len(a1)): ## cols
    for j in range(len(a2[0])):
        for k in range(len(a1[0])):
            a3[i][j] += a1[i][k] * a2[k][j]

print(a3)          

