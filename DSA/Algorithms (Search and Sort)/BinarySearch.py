
## time complexity is O(log N)
## the array must be in sorted order

k = [1,2,3,4,5,6,7,8,9]

target = 99
start = 0
end = len(k)-1

ans = False
while start<=end:
    mid = (start+end)//2
    if k[mid] == target:
        print("At index ", mid)
        ans = True
        break;

    elif k[mid] > target:
        end = mid - 1

    else:
        start = mid +1 

if ans==False: print("No such element in the array")

