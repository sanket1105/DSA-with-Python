
## Tuples:
## created using open and close paranthesis

cordinates = (4,5)
print(cordinates[0])

print("######################################################")
print("###############################################")

print(" list of tuples :")
coordinates = [(1,2),(3,4),(5,6)]
print(coordinates)
print(coordinates[0])


print("######################################################")
print("###############################################")

## functions in python

def sayhi():
    print("hello sanket")

sayhi()  

print("######################################################")
print("###############################################")

def cheese(name,age): ## assuming age is integer 
    print("hello "+ name)
    print("with age "+ str(age))

cheese("Sanket",21)


print("######################################################")
print("###############################################")


## return statement

def add(a,b):
    return int(a)+int(b)  ## simply a+b will be termed as a concatenation of string, so use int

result = add(5,6)
print(result)


## if statements

is_male = False

if is_male:
    print(" you are a male")
else :
    print(" not a male")    

print("######################################################")
print("###############################################")

is_male = True
is_tall = False

if is_male and is_tall:
    print("conditions satisfied")

elif is_male and not(is_tall):
    print("partial conditions are satisfied")

else :
    print(" no conditions satisfied")    

print("######################################################")
print("###############################################")

print(" if statements using compare statements :")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3    
        
print(max_num(3,40,5))   

print("######################################################")
print("###############################################")

print("Better Calculator :")
num1 = float(input("Enter the first number :"))
op = input("Enter the operator :")
num2 = float(input("enter the 2nd number :"))


def cal(num1,num2):
    if op=="+": print(num1+num2)
    elif  op=="-" : print(num1-num2)
    elif op=="*" : print(num1*num2)
    else: print(num1/num2)

cal(num1,num2)    
