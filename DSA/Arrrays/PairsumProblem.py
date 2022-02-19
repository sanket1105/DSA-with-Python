
def pairSum(arr,k):
    n = len(arr)
    for i in range(n):
        if k-arr[i] in arr:
     
            return True
    return False

print(pairSum([2,4,7,11,14,16,20,21],31))            