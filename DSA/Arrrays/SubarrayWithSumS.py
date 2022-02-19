
a = [1,2,3,8,5]
s= 12
n = len(a)

'''

for i in range(n):
    sum = a[i]
    for j in range(i+1,n):
        sum += a[j]
        if sum==s:
            print(i+1,j+1)
            break 
        elif sum>=s: continue    
        
        
'''

## optimized approach
# An efficient program 
# to print subarray
# with sum as given sum 

# Returns true if the 
# there is a subarray 
# of arr[] with sum
# equal to 'sum' 
# otherwise returns 
# false. Also, prints 
# the result.

def subArraySum(arr, n, sum_):
    
    # Initialize curr_sum as
    # value of first element
    # and starting point as 0 
    curr_sum = arr[0]
    start = 0

    # Add elements one by 
    # one to curr_sum and 
    # if the curr_sum exceeds 
    # the sum, then remove 
    # starting element 
    i = 1
    while i <= n:
        
        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while curr_sum > sum_ and start <= i-1:
        
            curr_sum = curr_sum - arr[start]
            start += 1
            
        # If curr_sum becomes
        # equal to sum, then
        # return true
        if curr_sum == sum_:
            print ("Sum found between indexes")
            print ("% d and % d"%(start, i-1))
            return 1

        # Add this element 
        # to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    # If we reach here, 
    # then no subarray
    print ("No subarray found")
    return 0

subArraySum(a,n,s)