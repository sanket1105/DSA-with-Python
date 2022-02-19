
from tkinter import N


arr = [1,2,3,4,5]
global n
n = 1e6

ans = [False] * int(n)

for i in range(len(arr)):
    if arr[i]>0:
        ans[arr[i]] = True

for i in range(1,len(ans)):
    if ans[i] == False:
        print("smallest number missing is: ",i)
        break

