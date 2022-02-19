
import array as arr 
a = arr.array('i',[1,2,3,4,99,6])
max = a[0]
for i in range(1,len(a)):
    if a[i]>max:
        max=a[i]
print("max: ", max)        