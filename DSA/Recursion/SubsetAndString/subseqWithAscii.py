
a = "abc"
def subseq(a,k):
    if len(a)==0:
        print(k)
        return 

    ## either take the element or ignore it
    subseq(a[1:],k+a[0]) ## taken
    subseq(a[1:],k) ##ignore    
    subseq(a[1:],k+str(ord(a[0]))) ## with ascii value



subseq(a,"")