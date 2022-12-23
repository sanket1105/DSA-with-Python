

'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
one of the numbers in s got duplicated to another number in the set, which results in repetition of one number 
and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
'''


k = [1,2,3,2,5]

i=0
while i<len(k):
    correctIndex = k[i]-1
    if k[i] != k[correctIndex]:
        k[i],k[correctIndex] = k[correctIndex],k[i]
    else:
        i+=1  
print(k)
ans=[]
for i in range(len(k)):
    if k[i] != i+1:
        ans.append(k[i])
        ans.append(i+1)
          
print(ans)


