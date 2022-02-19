arr = [1,2,3,4,5]
'''
48
20, 28
8, 12, 16
3, 5, 7, 9
1, 2, 3, 4, 5

'''
def PrintTriangle(arr):

    if len(arr)<1 : return 

    temp = [0] * (len(arr) - 1)

    for i in range(0,len(arr)-1):
        x = arr[i] + arr[i+1]
        temp[i] = x

    PrintTriangle(temp)
    print(arr)
    
   


PrintTriangle(arr)    

   