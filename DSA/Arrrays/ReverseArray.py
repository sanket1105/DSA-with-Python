
import array as arr 

a = arr.array("i",[1,2,3,4,5])
print("Array: ",a)
n = len(a)
for i in range(int(n/2)):
    a[i],a[n-1-i] = a[n-1-i],a[i]
print("reversed array ",a)

########################################################################
## Reverse using predeifned function

def reverse(arr1,n,start,end):
    while start<end:
        arr1[start],arr1[end] = arr1[end],arr1[start]
        start+=1
        end-=1
a= [1,2,3,4,5,6]
print(a)
n = len(a)
reverse(a,n,0,n-1)
print(a)

