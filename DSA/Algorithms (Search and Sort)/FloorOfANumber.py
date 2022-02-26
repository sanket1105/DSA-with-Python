
## Floor of a number means: greatest element in the array less than or equal to the target element

## same question as that of ceilings
## just the base equation will change

k = [1, 2, 8, 10, 10, 12, 19]
target = -1

start = 0
end = len(k) - 1
ans = False

if target < k[start] : 
        print("No floor exists in the given array")
        ans=True

else:
    while start<=end:
        mid = start + (end - start)//2
        

        if k[mid] == target:
            print("floor of the number is: ", k[mid])
            ans=True
            break;

        elif k[mid]>target:
            end = mid - 1
        else: start = mid + 1

if ans==False : print("floor of the number is: ",k[start-1])
    
    
