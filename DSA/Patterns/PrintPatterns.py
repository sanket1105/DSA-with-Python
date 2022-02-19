
'''
from the 2 for loops, outer for loop is for the number of rows
inner for loop is for the number of columns
so number of rows = number of time outer loop will run

Then find the number of columns in each row

'''

print(" Pattern 01")
rows=5
for i in range(0,rows):
    for k in range(0,i+1):
        print("*",end=" ")
    ## print new line    
    print("")   

##############################################  
print(" \n Pattern 02")
##################################################
rows = 5
for i in range(rows):
    for j in range(rows):
        print("*", end = ' ')
    print("")    
   

##############################################  
print(" \n Pattern 03")
##################################################

rows = 5
for i in range(0,rows):
    for j in range(0,rows-i):
        print("*",end=' ')
    print("")    


##############################################  
print(" \n Pattern 04")
##################################################  

n = 5
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1,end=" ")
    print("")  


##############################################  
print(" \n Pattern 05")
##################################################      

rows = 5
for i in range(1,2*n):
    c = i
    if c<=n:
        for j in range(1,c+1):
            print("*",end=' ')
    else:
        for j in range(1,2*n - c+1):
            print("*",end=" ")
    print('')                   


##############################################  
print(" \n Pattern 06")
##################################################    

rows = 5
for i in range(0,rows):
    for j in range(0,rows):
        if (i+j)>=rows-1:
            print("*",end=" ")
        else:
             print(" ",end=" ")
    print("")  

##############################################  
print(" \n Pattern 07")
##################################################    

rows = 5
for i in range(0,rows):
    for j in range(0,rows):
        if i<=j:
            print("*",end="")  ## no spaces between stars
        else:
             print(" ",end="")
    print("")  


##############################################  
print(" \n Pattern 08")
##################################################    

rows = 5

for i in range(0,rows):
    spaces = rows-i-1
    stars = 2*i + 1

    for j in range(spaces):  ## first print all the spaces
        print(" ",end='')
    for j in range(stars):  ## then print all the stars
        print("*",end="")   
    print("")               
        

##############################################  
print(" \n Pattern 09")
################################################## 

rows = 5
for i in range(0,rows):
    stars = 2*(rows-i)-1
    spaces = i

    for j in range(spaces):
        print(" ",end="")
    for j in range(stars):
        print("*",end='')

    print("")  


##############################################  
print(" \n Pattern 10")
##################################################  

rows = 5
for i in range(rows):
    stars = i+1
    spaces = rows-i-1

    for j in range(spaces):
        print(" ",end='')
    for j in range(stars):
        print("*",end=' ')  

    print("") 


 
##############################################  
print(" \n Pattern 11")
##################################################  

rows = 5
for i in range(rows):
    spaces = i
    stars = rows-i

    for j in range(spaces):
        print(" ",end='')
    for j in range(stars):
        print("*",end=' ')  

    print("")                  

##############################################  
print(" \n Pattern 12")
##################################################  


rows = 10
for i in range(0,rows):
    c = i
    if c<=4:
        stars = 5 - c
        spaces = c
        for j in range(spaces):
            print(" ",end='')
        for j in range(stars):
            print("*",end=" ")
            

    else:
        stars =  c - 4
        spaces = rows - c - 1
        
        for j in range(spaces):
            print(" ",end='')
        for j in range(stars):
            print("*",end=" ")


    print("")

#############################################  
print(" \n Pattern 13")
##################################################     

rows = 5
for i in range(0,rows):
    for j in range(0,2*rows-1):
        if (i+j)==4 or (j-i)==4 or i==4:
            print("*",end="")
        else:
            print(" ",end="")

    print("")        

#############################################  
print(" \n Pattern 14")
##################################################     

rows = 5
for i in range(0,rows):
    for j in range(0,2*rows-1):
        if (i+j)==8 or (i-j)==0 or i==0:
            print("*",end="")
        else:
            print(" ",end="")

    print("") 


#############################################  
print(" \n Pattern 15")
##################################################     

rows = 9
for i in range(0,rows):
    c = i
    if c<=4:
        for j in range(0,rows):
            if (i+j)==4 or (j-i)==4:
                print("*",end="")
            else:
                print(" ",end='')

    else:
        for j in range(0,rows):
              if (i-j)==4 or i+j==12:
                print("*",end='')
              else:
                print(" ",end='')
      

    print("")                        

#############################################  
print(" \n Pattern 16")
################################################## 



 



