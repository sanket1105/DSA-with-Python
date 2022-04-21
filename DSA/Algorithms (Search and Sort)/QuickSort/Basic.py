
## quick sort over merge sort: because
## it won't sort if the left or rigth arrray is already sorted
## but which merge sort does

## this algo makes the changes in the original one, doesn't create a new array
'''
You select any pivot, after each pass, all the elements less than the pivot will be in the left side
and all the elements greater than the pivot will be in the right side

The difference between merge and quick sort is that, 
in quick sort, if the array is sorted, it won't go to the base condition
whereas in merge sort, it was going till the base condition


How to put pivot at correct position:
Take the 2 pointers at start and end.
if the start is > pivot and end < pivot, swap those two and increment start and end pointers
Continue this process


How to pick the pivot:?
Say you picked any random element from total N elements:
say k elements to left of the picked element and (n-k-1) to right of the picked element,
T(N) = t(k) + t(n-nk-1) + O(n);  
 -> O(N) because, for putting the pivot at its correct place

 Worst case: you picked the pivot which is smallest or largest number : O(N**2)
 because either in the above case: the left or the right side will be empty

 So best is to select the middle element : (nlog(n))
 
'''
## notes
## 1. Not stable
## 2. Doesn't take extra place other than recursion, whereas in merge sort, we created a new array which took O(n) space
## 3. Merge sort is preferred in linked lists beacuse in LL, memory allocation is not continous whereas in arra, its is


def quicksort(nums,low,high):
    if low>=high: return 

    s=low
    e = high
    m = (s+e)//2
    pivot = nums[m]

    ## swapping condition
    while s<=e:
        while nums[s]<pivot:
            s+=1
        while nums[e]>pivot:
            e-=1   

         ## you reached a point where the condition fails
         ## swap the element if s<=e
        if s<=e:
            nums[s],nums[e] = nums[e],nums[s]  
            s+=1
            e-=1 

    ## now the pivot is at the correct index:
    ## lets call recursion for sorting 2 halves
    quicksort(nums,low,e)
    quicksort(nums,s,high)

nums=[6,5,9,8,6,22]
quicksort(nums,0,len(nums)-1)
print(nums)          





k = [1,2,3,5,0]
k.sort()