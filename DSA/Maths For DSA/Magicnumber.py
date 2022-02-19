
## write the number in bianry
## and multiply last digit with 5 power 1
## last second with 5 power 2
# and add all 


def magicNumber(n):
    result = 0
    x = 1
    j = 1
    while n:
        k = n & x
        result += k * (5**j)
        j += 1
        n = n>>1
    print(result)

magicNumber(6)

