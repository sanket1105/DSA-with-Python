

## enqueue:  add from the behind: rear
## deque: pop from the front

## while popping: if front points to null: then empty 

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = self.rear = None 

    def isempty(self):
        return self.front==None

    def enqueue(self,data):
        temp = node(data)
        if self.isempty():
            self.front = self.rear = temp
            return
        else:
            self.rear.next = temp
            self.rear = temp      

    def dequeue(self):
        if self.isempty(): return None

        else:
            self.front = self.front.next  

        if self.front == None:
            self.rear = None   

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)    

q.dequeue()
q.dequeue()
q.enqueue(40)    
print(q.front.data)
print(q.rear.data)