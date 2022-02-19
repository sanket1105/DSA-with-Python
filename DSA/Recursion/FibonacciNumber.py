
## print nth fibonacci number

## Linear Recurrence Relation

def fibonacci(n):
    if n<2: return n
    return fibonacci(n-1) + fibonacci(n-2)
    ## this will fail for finding the large fibonacci numbers
    ## since for every n, it will start from 0th fibo number
    ## Time complexity here is (golden ratio)^n


    ## see how this tree works in the recursion model
    ## built that recursion tree on your model
    ## and write down which functions goes in first on the stack, what removes and what again goes on the stack

print(" the fibonacci number is: ")
print(fibonacci(2))


## tail recursion: the last function call
## here in the above function, the last statement is not the tail recursion,
## since addition is performed, just fibonacci(n-1) should have been there, it would have been called, tail recursion

