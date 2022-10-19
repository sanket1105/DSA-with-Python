
arr = [ 10, 5, 3, 4, 3, 5, 6 ]
n = len(arr)
a = [0]*(max(arr)+1)
print(a)
found = False

for i in range(n):
    if a[arr[i]]!=0:
         print(arr[i])
         found = True
         break
    else: a[arr[i]] = 1

if found == False:
    print("No repeating element") 