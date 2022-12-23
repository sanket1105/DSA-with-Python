

## making deque as costly

class queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self,x):
        self.s1.append(x) 
        

    def dequeue(self):
        if len(self.s1)==0 and len(self.s2)==0:
            print("Queue is empty") 
            return

        elif len(self.s2)==0 and len(self.s1)>0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
            return self.s2.pop()

        else:
            return self.s2.pop()   

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())                




