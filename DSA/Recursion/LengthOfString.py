
string1 = "Sanket"

def LengthOfString(string1):
    if string1=="": return 0 ## if string is null
    else: 
        return 1+LengthOfString(string1[1:])

 

print(LengthOfString(string1))  
