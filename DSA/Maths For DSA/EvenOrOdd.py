

## if the last digit of the number is 1 in bimary form : its odd
## or else its even 

## so just perform the and operation betweenn the number and 1
### is result is 1: then odd
## else even 

n = [1,2,3,4,5,6]

for i in n:
    print(i," ", i & 1)