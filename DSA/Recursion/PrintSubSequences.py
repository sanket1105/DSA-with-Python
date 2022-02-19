 

def subsequences(str,idx,newstr):

     if idx==len(str):
         print(newstr)
         return

     newchar = str[idx]
    ## to be
     subsequences(str,idx+1,newstr+newchar) 

    ## not to be
     subsequences(str,idx+1,newstr)

str = "abc"
subsequences(str,0,"")        


## see its time complexity in the video