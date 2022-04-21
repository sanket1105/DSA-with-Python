
## remove all the A's from the string

s = 'sanket'

def removeA(a,k):

    if len(s)==0:
        return k
    elif a[0]=='a':
        removeA(a[1:],k)
    else:
        k+=a[0]

removeA(s,"")