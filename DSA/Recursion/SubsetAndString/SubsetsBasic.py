
## subset Pattern: the pattern of taking some element and removig some is SUBSET Pattern

## in printing all the subsequences: the element is either taken or not taken
'''
Subsets of a string:

"abc" -> a b c ab ac bc abc 
'''

a = "abc"
def subseq(a,k):
    if len(a)==0:
        print(k)
        return 

    ## either take the element or ignore it
    subseq(a[1:],k+a[0]) ## taken
    subseq(a[1:],k) ##ignore    


subseq(a,"")    

