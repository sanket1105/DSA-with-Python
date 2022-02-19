
## we will break the power in binary form
## and will take the places where the digit is one only
## say 6 as 4 +2 
## 6 as 110 in binary
## we will take just starting 2 pos


def aPowerB(base,power):
    ans = 1

    while power>0:
        if (power&1)==1:
            ans *= base

        base *= base
        power = power>>1

    print(ans)

aPowerB(2,6)

