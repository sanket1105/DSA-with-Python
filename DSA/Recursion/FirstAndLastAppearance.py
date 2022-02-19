
first,last = -1,-1

def firstAndLastAppearance(str,element,idx):
   
    global first,last
    if idx==len(str)-1: 
        print(first,last)
        return

    CurrentChar = str[idx]
    if CurrentChar==element:
        if first==-1: first=idx
        else : last = idx

    firstAndLastAppearance(str,element,idx+1) 


firstAndLastAppearance("abaacdaef","a",0)
   



