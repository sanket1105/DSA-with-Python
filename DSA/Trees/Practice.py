


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

    print(a[q[0]], end=  " ")

    while q and q[0] <= i-k:
        q.popleft()

    while q and a[i] >= a[q[-1]]:
        q.pop()
    q.append(i)        

print(a[q[0]])