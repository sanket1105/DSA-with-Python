
t = 12345

def sumOfDigits(n):
    if n==0: return 0
    return (n%10 + int(sumOfDigits(n/10)))

print(sumOfDigits(12345))    