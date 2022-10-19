
## stacks: LIFO 
## queue: FIFO

## stack: insertion and deletion occurs on same end
## queue: insertion and deletion occurs on diff. end

## this pop and append is taking O(n) time on the last stack
## so thats why we use the deque operation from collections library
## it just takes O(1) time
  
## stack: Push and Pop
## queue: Enqueue and Dequeue

stack = []
stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

print(stack.pop())
print(stack) 


################################################################
from collections import deque
stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')

print(stack)


print(stack.pop())
print(stack) 