

def countzeroes(n,count):
    if n==0: return count

    rem = n%10
    if rem==0: return countzeroes(n//10,count+1)
    else: return countzeroes(n//10,count)


print(countzeroes(10005,0))