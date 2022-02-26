
## there are no duplicates in the given array

def search_in_rotated_array(nums,target):

        def pivot(start,end):
                while start<=end:
                    mid = (start+end)//2

                    if mid<end and nums[mid]>nums[mid+1]:
                        return mid
                    if mid>start and nums[mid] < nums[mid-1]:
                        return mid-1
                    if nums[mid]<=nums[start]:
                        end = mid-1
                    else: start = mid+1
                        
                return -1       

    
        def binary_search(start,end):
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid] > target:
                    end = mid-1
                else: start = mid+1
            return -1
        
        
        pivot_ele = pivot(0,len(nums)-1)
        
        if pivot_ele == -1:  ## if no pivot: that is array is already sorted
            return binary_search(0,len(nums)-1)
        else:
            if nums[pivot_ele]==target: return pivot_ele
            elif target>=nums[0]:
                return binary_search(0,pivot_ele)
            else:
                return binary_search(pivot_ele+1,len(nums)-1)


nums =[4,5,6,7,0,1,2]
target = 2

print("given element at index: ")
print(search_in_rotated_array(nums,target))