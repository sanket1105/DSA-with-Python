
a = [1,2,3,8,5]
s= 16
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

    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum_ and start <= i-1:
        
            curr_sum = curr_sum - arr[start]
            start += 1
   
        if curr_sum == sum_:
            print ("Sum found between indexes")
            print ("% d and % d"%(start, i-1))
            return 1

        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    print ("No subarray found")
    return 0

subArraySum(a,n,s)