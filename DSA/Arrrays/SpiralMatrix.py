
a= [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def spiral(matrix):
    
    k =[]
    if len(matrix)==0: return k
    colbegin,rowbegin = 0,0
    rowend = len(matrix)-1
    colend = len(matrix[0])-1

    while (colbegin <= colend and rowbegin <= rowend):

        for i in range(colbegin,colend+1):
            k.append(matrix[rowbegin][i])
        rowbegin += 1

        for i in range(rowbegin, rowend+1): 
            k.append(matrix[i][colend])
        colend -= 1

        if rowbegin<=rowend:
            for i in range(colend,colbegin-1,-1):
                k.append(matrix[rowend][i])
            rowend -= 1    

        if colbegin<=colend:
            for i in range(rowend,rowbegin-1,-1):
                k.append(matrix[i][colbegin])
            colbegin += 1

    return k

print(spiral(a))
print("\n")
print(spiral(b))




