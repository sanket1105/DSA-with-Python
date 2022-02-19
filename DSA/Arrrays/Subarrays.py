
## subarray : continous elements from the arrray
## number of subarrays for an array will be :
## nC2 + n  : (nc2 means take any two elements and n since each element can also be sb array)


## subsequence: take random elements but their order should be same as that in array
## in subsequnce : each entry in array has choice whether to be part of the subsequence or not



## sum of each possible subarrays 

nums = [1,2,0,7,2]
for i in range(len(nums)):
    sum = 0
    for j in range(i,len(nums)):
        sum += nums[j]
        print(sum)

