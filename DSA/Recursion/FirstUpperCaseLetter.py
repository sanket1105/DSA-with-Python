
def Uppercase(str,start,end):
    if start>end: return -1

    elif str[start].isupper(): return start
    else : return Uppercase(str,start+1,end)

print("First Capital Letter is at index number: ")

str='sankeT'
print(Uppercase(str,0,len(str)-1))    

