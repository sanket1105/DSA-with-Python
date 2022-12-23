
## binary Search
## time complexity is O(log N)
## the array must be in sorted order

k = [1,2,3,4,5,6,7,8,9]
end = len(k)-1
start = 0
target = 19
found = False
while start<=end:
    mid = (start+end)//2
    if k[mid]==target:
        print("found")
        found = True
        break
    elif k[mid] > target:
        end = mid-1
    else: start = mid+1
if found== False: 
    print(" Not there")    

#############################################
## selection sort
## Select the min element is put at at its correct place thats is its correct index
#We will go on selecting the min element and will put that element in the right spot
## O(n**2)

k = [2,2,1,1,1,8,2,2]

for i in range(len(k)):
    min = i
    for j in range(i,len(k)):
        if k[j] < k[min]:
            min = j
    k[i],k[min] = k[min],k[i]        

print(k)

###############################################################

## bubble sort
#In this first pass, the largest element comes in the end and so on....on each step
## no extra space used : O(1)
## time complexity : O(n**2)

k = [2,2,1,1,1,2,2]
n = len(k)
for i in range(n):
    swap = False
    for j in range(1,n-i):
        if k[j-1] > k[j]:
            k[j-1],k[j] = k[j],k[j-1]
            swap=True

    if swap==False: 
        break
print(k)    

##############################################

## insertion sort

# Sorting the array partially.
# that is firt sort till index 1 then index 2 then index 3 and so on.
# So for every element, its left side is sorted, so put the current index at its particular place in the LHS
# ## after every pass: left side is getting sorted
# Worst case : O(n^2)
# Best Case: O(n) : already sorted
# Why insertion sort: Steps get reduced as a result, number of swaps get reduced as a result
# ## its stable
# ## use for smaller values for n
# ## works good when array is partially sorted


k = [2,2,1,1,1,2,2]
n = len(k)

for i in range(n):
    for j in range(i,0,-1):
        if k[j-1]>k[j]:
            k[j-1],k[j] = k[j],k[j-1]
        else:
            break
print(k)            
#######################################################################################################

## cyclic sort:
## array needs to have elemets from 1 to n

k = [1,5,3,4,2]
i = 0
while i < len(k):
    correctindex = k[i]-1
    if k[i] != k[correctindex]:
        k[i],k[correctindex] = k[correctindex],k[i]   
    else:
        i+=1
print(k)            

#########################################################################################################

def mergesort(left,right):
    ans = [0]* (len(left) + len(right))
    i,j,k = 0,0,0

    while i < len(left) and j<len(right):
        if left[i] < right[j]:
            ans[k] = left[i]
            i+=1
        else:
            ans[k] = right[j]
            j+=1
        k+=1

    ## if the array  isn't finished
    while i < len(left):
        ans[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        ans[k] = right[j]
        j+=1
        k+=1

    return ans    


def merge(arr):
    if len(arr)==1: return arr

    mid = len(arr)//2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    return mergesort(left,right)

nums = [5,9,8,5,3,6,7,4]

print(merge(nums))   



###########################################################################################
## selection sort
k = [6,5,9,4,5,9,8,7]
n = len(k)

for i in range(n):
    min = i
    for j in range(i,n):
        if k[j] < k[min]:
            min = j
    k[i],k[min] = k[min], k[i]   

print(k)

####################################################################
## bubble sort
k = [6,5,9,4,5,9,8,7]
n = len(k)
for i in range(n):
    swap = False
    for j in range(1,n-i):
        if k[j-1] > k[j]:
            k[j-1],k[j] = k[j],k[j-1]
            swap = True
    if swap == False:
        break
print(k)         

###################################################################################
## insertion sort
k = [6,5,9,4,5,9,8,7]
n = len(k)

for i in range(n):
    for j in range(i,0,-1):
        if k[j] < k[j-1]:
            k[j],k[j-1] = k[j-1],k[j]
        else:
            break
print(k)            



##################################################################
# ceiling of a numbert
k = [1, 2, 8, 10, 10, 12, 19]
target = 20

start = 0
end = len(k)-1
found = False

if target > k[end]:
    print("No ceiling exists")
    found = True
else:    
    while start<=end:
        mid = (start+end)//2
        if k[mid] == target:
            print("ceiling is: ", k[mid])
            found = True
            break
        elif k[mid]>target:
            end = mid-1
        else: start = mid+1     

if found==False:
    print("ceiling is: ", k[start])



######################################################################
# rotations
arr = [4,5,6,7,0,1,2]

def pivot(k):
    start = 0
    end = len(k)-1

    while start<end:
        mid =  (start+end)//2

        if mid<end and k[mid]>k[mid+1]:
            return mid
        if mid>start and k[mid-1] > k[mid]:
            return mid-1
        if k[start] >= k[mid]:
            end = mid-1   
        else: start = mid+1
    return -1

ans = pivot(arr)
if ans == -1: print("No rotations")
else: print(ans+1," rotations")


######################################################
# finding duplicate element in the array
nums = [2,1,2,3]

i = 0
while i < (len(nums)):
    corrindex = nums[i]-1
    if nums[i]!=nums[corrindex]:
        nums[i],nums[corrindex] = nums[corrindex],nums[i]
    else: 
        i+=1

print(nums)
print("repeating element is : ",nums[-1])

###########################################################
# first missing positive element
nums=[-1,4,2,1,9,10]
i = 0
while i < (len(nums)):
    corrindex = nums[i]-1
    if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[corrindex]:
        nums[corrindex],nums[i] = nums[i],nums[corrindex]
    else: i+=1

print(nums)

found = False
for i in range(len(nums)):
    if nums[i]!=i+1:
        print(i+1)
        found = True
        break

if found==False: print(nums[i]+1)

###################################################################
# set mismatch
k = [1,2,3,2,5]
i = 0
while i< len(k):
    corrindex = k[i]-1
    if k[i]!= k[corrindex]:
        k[i],k[corrindex] = k[corrindex],k[i]
    else: i+=1
print(k)        

ans = []
for i in range(len(k)):
    if k[i]!=i+1:
        ans.append(k[i])
        ans.append(i+1)
print(ans)        
