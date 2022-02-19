
arr = [1, 4, 3, -5, -4, 8, 6]

def MaxInArray(arr,N):
    if N==0 : return arr[0]

    return max(arr[N-1],MaxInArray(arr,N-1))

print(" max in array is:")
print(MaxInArray(arr,len(arr)-1))

## same goes for min value using recursion

arr.sort()
print(arr)

print(sorted(arr))