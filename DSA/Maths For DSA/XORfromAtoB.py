

## its XOR from a to b
## we have already done 0 to b
## so just do XOR from 0 to b and then XOR from 0 to a-1

## it will remove the XOR already done in 0 to break

def XORfromAtoB(a,b):
    arr1 = [b,1,b+1,0]
    till_b = arr1[b%4]

    a = a-1
    arr2 = [a,1,a+1,0]
    till_a = arr2[a%4]

    print((till_b ^ till_a)) 

XORfromAtoB(3,9)
