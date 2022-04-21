
## remove all the A's from the string

s = 'aaaaaaab'

def removeA(a,k):

    if len(a)==0:
        print(k)
        return

    ch = a[0]
    if ch=='a':
        removeA(a[1:],k)
    else:
        removeA(a[1:],k+ch)    

removeA(s,"")
