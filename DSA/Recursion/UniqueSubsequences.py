 

def subsequences(str,idx,newstr,myset):

     if idx==len(str):
         if newstr in myset:
             return
         else : 
             print(newstr)  
             myset.add(newstr)  
             return

     newchar = str[idx]
    ## to be
     subsequences(str,idx+1,newstr+newchar,myset) 

    ## not to be
     subsequences(str,idx+1,newstr,myset)

str = "aaa"
myset = set()
subsequences(str,0,"",myset)        


## see its time complexity in the video