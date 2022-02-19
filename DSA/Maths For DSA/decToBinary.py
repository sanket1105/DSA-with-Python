
def dToB(n):
    if n>1:
        dToB(n//2)
    print(n%2, end = " ")

def bToD(n):
    i,decimal = 0,0
    while n!= 0:
        rem = n%10
        decimal = decimal + rem * pow(2,i)
        n = n//10
        i += 1

    print(decimal, end = " ")    

dToB(17)
print("")
bToD(10001)

        