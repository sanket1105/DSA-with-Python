
def ProductOfTwo(i,j):
    if i==0 or j==0: return 0

    elif j>i: ProductOfTwo(j,i)  ## swap so that less number of iterative sols

    return (i + ProductOfTwo(i,(j-1)))


print(ProductOfTwo(100,5)) 