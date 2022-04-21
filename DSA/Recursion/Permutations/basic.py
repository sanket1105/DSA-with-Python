
a = 'abc'

def permutation(a,k):
    if len(a)==0:
        print(k)
        return

    for i in range(len(k)+1): ## different places where next character can be permutation
        ## say if length of k is 2: so new char can got at 0,1 or 2th index
        f = k[:i]
        s = k[i:]
        permutation(a[1:],str(f)+str(a[0])+str(s))

permutation(a,"")