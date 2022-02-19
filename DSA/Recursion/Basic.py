
### why recurison? Helps in solvig bigger/complex problems in a simpler way
### Space complexity is not constant bcoz of recursion calls. Thats the con of recursion

print("Hello world")


### print "Hello World" 5 times
print("\ninside the recursion function \n")
def recur(i):
    for k in range(i):
        print("Hello World")

recur(5)


## Print starting 5 numbers:
print("\n Numbers funtion \n")

def Numbersfunction(i):
    if i==5 :   ## base condition : where function stops making recursive calls
        print(i)
        return

    print(i)    
    Numbersfunction(i+1)

Numbersfunction(1)    