
def ReverseString(s):
    if s=="": return 

    temp = s[0]
    ReverseString(s[1:])
    print(temp,end="")


ReverseString("Sanket")    
    