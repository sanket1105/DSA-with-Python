
## ceiling of a number means: smallest element in the array greater than or equal to the target element

k = [1, 2, 8, 10, 10, 12, 19]
target = 20

start = 0
end = len(k) - 1
ans = False

if target > k[end] : 
        print("No ceiling exists in the given array")
        ans=True

else:
    while start<=end:
        mid = start + (end - start)//2
        

        if k[mid] == target:
            print("Ceiling of the number is: ", k[mid])
            ans=True
            break;

        elif k[mid]>target:
            end = mid - 1
        else: start = mid + 1

if ans==False : print("Ceiling of the number is: ",k[start])
    
    
