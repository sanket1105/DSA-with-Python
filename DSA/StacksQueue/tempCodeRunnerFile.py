
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