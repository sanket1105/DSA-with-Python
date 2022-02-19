
## lets say we are just playing till 8th bit
## and elements are repeating thrice except one
Int_size = 8
def unique(arr):
    result = 0
    for i in range(Int_size):
        sm = 0
        x = 1<<i
        for j in arr:
            if j & x:
                sm += 1
        if sm%3!=0:        
            result = result | x

    print(result)

unique([5,5,5,3])
