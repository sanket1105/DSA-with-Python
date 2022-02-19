
def NaturalSum(n):
    if n==1: return n
    return n + NaturalSum(n-1)

print(NaturalSum(5))    