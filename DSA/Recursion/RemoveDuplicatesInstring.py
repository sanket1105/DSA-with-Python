
l1 = [False]*26

def removeDuplicates(str,idx,newstr):

    if idx==len(str):
        print(newstr)
        return

    currchar = str[idx]
    if l1[ord(currchar)-ord('a')]==True: ## if already there
        removeDuplicates(str,idx+1,newstr)
    else:
        newstr+=currchar  
        l1[ord(currchar)-ord('a')] = True  
        removeDuplicates(str,idx+1,newstr)


removeDuplicates("aabbccdd",0,"")

