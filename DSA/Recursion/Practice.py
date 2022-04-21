

def rev(n):
    if n%10==n: return n

    return str(n%10) + str(rev(n//10))

print(rev(23450))    