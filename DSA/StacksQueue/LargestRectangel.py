
'''
Array represents the height of the histrograms bar and width of each bar is 1
Area of largest rectangle

a = [2,1,5,6,2,3]
max length is 5 and 5,6 alternate so width = 2
area = 5*2 = 10
'''

'''
## brute force
import math
a = [2,1,5,6,2,3]
ans = 0
n = len(a)

for i in range(n):
    min_h = math.inf
    for j in range(i,n):
        min_h = min(a[j],min_h)
        len = j-i+1  ## width between j and i
        ans = max(ans,len*min_h)

print(ans)
'''

## create a stack, once you get a bar height less than the previous bar,
## then calculate the area of previous bar and pop it off the stack

a = [2,1,5,6,2,3]

ans = 0
stack = [-1]  ## indexes of buildings with ascending heights
height = a + [0]


for i in range(len(height)):
    while height[i] < height[stack[-1]]:
        h = height[stack.pop()]
        w = i - stack[-1] - 1  ## -1 because we did stack.pop() : so it got 1 element back: so width increased by 1, so we did -1 so as to keep tehe width intact
        ans = max(ans,h*w)
    stack.append(i)
height.pop()
print(ans)        




   


