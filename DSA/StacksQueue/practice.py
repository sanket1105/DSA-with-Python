
from secrets import randbits


a = [2,1,5,6,2,3]
stack = [-1]
ans = 0
a.append(0)

for i in range(len(a)):
    while a[i] < a[stack[-1]]:
        h = a[stack.pop()]
        w = i - stack[-1] - 1
        ans = max(ans,h*w)
    stack.append(i)

print(ans)

##################################################################
a = [2,1,5,6,2,3]

stack = []
ans = 0

for i in range(len(a)):
    while stack and a[i] > a[stack[-1]]:
        curr_height = a[stack.pop()]
        if len(stack)==0 : break
        height = min(a[i],a[stack[-1]]) - curr_height
        width = i - stack[-1] - 1
        ans+=height*width
    stack.append(i)

print(ans)

#################################################################
ans = "(a+(b)/c)"
stack  =[]
open = ['(','{','[']
close = [')','}',']']
keys = ['+','-','*','/']
found = False

for i in ans:
    if i in open or i in keys:
        stack.append(i)
    if i in close:
        k = stack.pop()
        if k not in keys:
            found = True
            break
        elif k in keys:
            stack.pop()

if found==False: print("False")
else: print("True")


######################################################

price = [10, 4, 5, 90, 120, 80]
ans = [0]*len(price)
n = len(price)
stack = [0] ## initialize the stack
ans[0] = 1 ## for first element : frequency == 1

for i in range(1,n):
    while stack and price[i] >= price[ans[-1]]:
        stack.pop()
    ans[i] = (i+1) if len(stack)<=0 else i-stack[-1] 

print(max(ans))

################################################################
## triplets
a = [1, 4, 45, 6, 10, 8]
sum = 22
n = len(a)
a.sort()

found = False
for i in range(n-2):
    l = i+1
    r = n-1

    while l < r:
        if a[i] + a[l] + a[r] == sum:
            found = True
            print(a[i],a[l],a[r])
            break

        elif  a[i] + a[l] + a[r] > sum:
            r-=1
        else:
            l+=1

if found==False: print("No such triplet exists")


######################################################################
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
start,end,n = 0,0,len(nums)
zerocount = 0
ans=  0

while end < n:
    if nums[end]==0:
        zerocount += 1

    while zerocount > k:
        if nums[start]==0:
            zerocount -= 1
        start += 1

    ans = max(ans,end-start+1)
    end+=1
print(ans)            


##############################################
a = [2,1,5,6,2,3]
ans = 0
q = []

for i in range(len(a)):
    while q and a[i] > a[q[-1]]:
        curr_height = a[q.pop()]
        if len(q) == 0: break
        h = min(a[i],a[q[-1]]) - curr_height
        w = i-q[-1]-1
        ans+=h*w
    q.append(i)

print(ans)        