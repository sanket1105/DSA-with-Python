


## in python, there are no priitives, everything is an object
## but in java, primitives(int, float, bollean, char....) are stored in stack
## whiile object are stored in heap type

##primitives : something that cannot be broken down furthur
## non-primitives : something that can broken down : arrays, strings...

## the type of data in the array should be same

## the space for the array is alloated at run time
## so its dynamic memory allocation
## declaration for array is done at compile time
## memory allocation at run time

'''
## array objects are stored in heap.
## Heap objects are not continous
## and memoery allocation using DMA
## so theres a chance thar array in python are not continous
'''

import array as arr

a = arr.array('i',[1,2,3,4,5])
print(a)
print(type(a))

b = arr.array('d',[1,2,3,4,5.55])
print(b)
print(type(b))


print("array befor insertion: ")
for i in a:
    print(i,end=" ")

print("\n array after insertion: ")
a.insert(1,99) ## insert 99 at pos index 1
for i in a:
    print(i,end=" ")
print("\n")    

################################################################

k = [11,22]
for i in k:
    s = list(i)  ## cannot form list for input data type as int
    print(s)   
#########################################################
## pop in python

print(a[0])
print(a.pop()) ## by deafult will remove the last element
print(a)
print(a.pop(0)) ## removes elememt from index 0
print(a)

################################################################

## remove in python: use to remove the first occurence of element from

a = arr.array('i',[1,2,3,3,4,5,9,6,9,6,6,6])
a.remove(3)
print(a) ## first 3 got removed

###############################################################

## index to print the first occurence of any value in list
l=[1,2,2,3,4,5,6,7,8,9]
a = arr.array('i',l)
print("first occurence is 2 is at index : ",a.index(2))

###############################################################

## updating elements:
print(a)
a[0]=55
print(a)

################################################################

a = []
## print(a[0]) : out of index range

a = None  
print(type(a))
print(a)

###########################################################

## List  to String
a = ["Hello","I","am","Sanket"]
b = " ".join(a)
print(b)

## str() use to convert other data type to str
c = " ".join(str(e) for e in a)
print(c)

d = " "
for i in a:
    d+=" "+i
print(d)  

e = " ".join(map(str,a))
print(e)
###############################################

## 2d arrays

rows,cols = 5,5
k = [[0]*cols]*rows
print(k)

k = [[0 for i in range(cols)] for j in range(rows)]
k

a=[]
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append(0)
    a.append(col)
print(a)  

## SEE the difference in output
rows,cols = 5,5
a = [[0]*cols]*rows
a[0][0] = 1
for row in a:
    print(row)

## see the diff in output
a = [[0 for j in range(cols)] for i in range(rows)]   
a[0][0] = 1
for rows in a:
    print(rows)

## https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
## read this to get what is happeing in the above two examples

a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print("")


################
#########################################

import numpy as np 
l1 = [1,2,3]
l2=[4,5,6]

vector1 = np.array(l1)
vector2 = np.array(l2)
answer = vector1.dot(vector2)
print(answer)

k = vector1*5
print(k)

import numpy as np
l1 = [1,2,3]
l2=[4,5,6]
vector1 = np.array(l1)
vector2 = np.array(l2)
answer = vector1+(vector2)
print(answer)


print(type(int("123")))


k=[]
k.append([1,2,3])
k.append([5,6])
print(k)

matrix = [[0,1,1],[1,0,1],[2,1,1]]
m=0
matrix[:][:][0]



