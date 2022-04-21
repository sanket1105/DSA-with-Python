
## queue: FIFO
## queue: used in list


## use deque so that the operation gets done in O(1) thing

'''
Enqueue: adds an item to the list
deque: removes an item
'''

queue=[]
queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

print(queue.pop(0))
print(queue)


################################################################################################

from collections import deque

queue = deque()
queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

print(queue.popleft())
print(queue)

#####################################################################

## inbuilt function

from queue import Queue
q = Queue(maxsize=3)

print(q.qsize())

q.put('a')
q.put('b')
q.put('c')

print(q.full())

## to pop:  use q.get()
print(q.get())
print(q.get())