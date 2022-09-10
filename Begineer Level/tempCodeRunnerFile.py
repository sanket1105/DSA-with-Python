
## 2d lists  

number_grid =  [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print("len of array : ")
print(len(number_grid))
## grid of 4 rows and 2 columns

print("\n")
print(number_grid[0][1])

print("\n")
## nested for loops

for  row in number_grid:
    for col in row:
        print(col,end=" ")
    print("\n")    

print("\n")


print("####################################################")
print("####################################################")


## language translator
## vowels to 'g' or "G" letter

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else :    
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation  

print(translate("Occupy"))    

##====================================================================================

'''
Sanket Zanwar New way of writing comment

'''



print("####################################################")
print("####################################################")


## try and expect : use to catch the errors

 ## suppose you asked for integer entry
 ## but you got string as an input
 ## its obvious that computer will throw the error
 ## but to catch the error before computer throws
 ## at that time we will use try-except

try:
     number = int(input("enter the number: "))
     print(number)
except:
    print("invalid input")   

## now the computer wont yell at us
## it will just show the statement written in except function  

try:
     value  = 10/0
     number = int(input("enter the number: "))
     print(number)

except ZeroDivisionError:
    print("Divided by zero")

except ValueError:
    print("invalid input")


print("################################################################")    
print("################################################################")    


### reading the file
'''
r->read
w-> write
a-> append
r+ -> read and write

'''
## change the path where you wanna store the employees file
import os
os.chdir("E:\\Python VS Codes\\Begineer Level")


employee_file = open("employees.txt","r")

## check whthere is it readable or not
print(employee_file.read())

print("###########################################")

print(employee_file.readline())

employee_file.close()

print("######################################################")

employee_file = open("employees.txt","a")
employee_file.write("toby - Human Resources")
employee_file.close()

## now here you want the thing to be appended at the end that is in new line

employee_file = open("employees.txt","w")
employee_file.write("\n Kelly- customer Service")
employee_file.close()


print("##################################################")
print("##################################################")

## module is the file that we can import into the python
## now importing the TempFile and using the functions defined in that file

print("import the required file")
import TempFile  ## import the file u wanna import

## roll_dice is the function predefined in the imported file
print(TempFile.roll_dice(10))

print("##################################################")
print("##################################################")

## pip is the package manager
## it allows you to manage, install, uninstall the package


## now that we have install python-docx module from the net using command prompt
## lets import that

import docx
## now see the different functions available under it
## type this -> docx.
## you will see the list of functions available