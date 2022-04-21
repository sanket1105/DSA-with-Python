
## subsequences of the string

#3 return the array list now 
## instead of putting the chars in the new string


a='abc'

def subseq(a,k):

    if len(a)==0:
        ans=[]
        ans.append(k)
        return ans

    left = (subseq(a[1:],k+a[0])) ## taken
    right = (subseq(a[1:],k))
    
    left += right
    return left  

print(subseq(a,""))
