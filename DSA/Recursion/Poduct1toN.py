
from math import prod


def multiplication(N):

    if N==1: return 1
    return N*multiplication(N-1)
    


multiplication(5)
