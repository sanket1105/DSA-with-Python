  
## its an doubly ended queue
## insert and delete from both front and back

from collections import deque
d = deque()

d.append('b')
d.append('c')
d.insert(0,'a')

print(d)
print(d.pop()) ## same as stack
print(d)
print(d.popleft())  ## same as queue