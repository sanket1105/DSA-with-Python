
## balanced parenthesis or not

def balanced(str):
    open = ['{','(','[']
    close = ['}',')',']']

    stack = []
    for i in str:
        if i in open:
            stack.append(i)
        elif i in close:
            pos = close.index(i)   

            if len(stack)>0 and open[pos] == stack[-1]  :
                stack.pop()
            else: 
                return "unbalanced"

    if len(stack)==0: return "balanced"
    else: return "unbalanced"    

string = "{[]{()}}"
print(string,"-", balanced(string))
  
string = "[{}{})(]"
print(string,"-", balanced(string))
  
string = "((()"
print(string,"-",balanced(string))                    

#######################################################################
## reverse the sentence

stack = []
s = 'Hey, I am Sanket.'
ans= ""
for i in s:
    if i!=" ": ans+=i

    else: 
        stack.append(ans)
        ans = ""

stack.append(ans)

while len(stack):
    print(stack.pop(), end = " ")

###################################################################
#sliding window maximum

a = [1,3,-1,-3,5,3,6,7]
k = 3
n = len(a)

from collections import deque
q = deque()

for i in range(k):
    while q and a[i] > a[q[-1]]:
        q.pop()
    q.append(i)

for i in range(k,n):
    print(a[q[0]])

    while q and q[0]<=i-k:
        q.popleft()

    while q and a[i] > a[q[-1]]:
        q.pop()
    q.append(i)
print(a[q[0]])    

##################################################################
## largest rectangle

a = [2,1,5,6,2,3]
stack =[-1]
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
## trapping rain water

a = [3,1,2,4,0,1,3,2]
stack = []
ans = 0
for i,heighta in enumerate(a):
    while stack and heighta > a[stack[-1]]:
        currheight = a[stack.pop()]
        if not stack: 
            break
        j,heightb = stack[-1], a[stack[-1]]
        volume = min(heighta,heightb) - currheight
        ans+=volume * (i-j-1)
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
    r = n-2

    while l<r:
        if a[i]+a[l]+a[r] == sum:
            found  = True
            print(a[i],a[l],a[r])
            break

        elif a[i]+a[l]+a[r] > sum:
            r = r-1
        else: l+=1    

if found == False: print("Not found")


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