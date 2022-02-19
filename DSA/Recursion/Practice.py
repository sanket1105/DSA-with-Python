
def sumtriangle(arr):

    if len(arr)<1 : return

    temp = [0]*(len(arr)-1)
    for i in range(0,len(arr)-1):
        temp[i] = arr[i] + arr[i+1]

    sumtriangle(temp) 
    print(arr)
     

arr=[1,2,3,4,5]

sumtriangle(arr)