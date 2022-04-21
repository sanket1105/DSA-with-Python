 
'''
You are given the array and a value k: that is size
so your job is to find the max value from the array considering the size k each time

array = [1,3,-1,-3,5,3,6,7]
ans: [3,3,5,5,6,7]

'''
  
'''
## normal method
a = [1,3,-1,-3,5,3,6,7]
k = 3
ans = []

for i in range(len(a)-k+1):
    max = a[i]
    for j in range(k):
        if a[i+j] > max:
            max = a[i+j]
            ans.append(max)
print(ans)    

'''
## using dequeue

from collections import deque
a = [1,3,-1,-3,5,3,6,7]
k = 3
n = len(a)

q = deque()
for i in range(k):
    while q and a[i] >= a[q[-1]]:
        q.pop()
    q.append(i)   

for i in range(k,n):

    print(a[q[0]],end=" ")

    ## remove the element from the previous sub array of size k
    while q and q[0] <= i-k:
        ## since i-k will not be part of current window
        q.popleft()

    while q and a[i] >= a[q[-1]]:
        q.pop()
    q.append(i) 

print(a[q[0]],end=" ")       




        



