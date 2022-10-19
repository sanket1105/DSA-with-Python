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