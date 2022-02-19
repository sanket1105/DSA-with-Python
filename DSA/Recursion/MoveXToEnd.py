
def moveXToEnd(str,idx, count,newstr):

    if idx==len(str):
        newstr+='x'*count
        print(newstr)
        return

    if str[idx]=="x":
        count+=1
        moveXToEnd(str,idx+1,count,newstr)

    else:
        newstr+=str[idx]
        moveXToEnd(str,idx+1,count,newstr)


moveXToEnd("axbcxxd",0,0,"")     


print(len("axbcxxd"))