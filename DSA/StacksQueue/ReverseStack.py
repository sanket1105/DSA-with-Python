

class stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100  ## max length of 100

    def isempty(self):
        if self.top==-1:
            return True
        else: return False

    def isfull(self):
        if self.top == self.max - 1 :
            return True
        else: return False

    def push(self,data):
        if self.isfull():
            print("Stack Overflow")
            return
        else:
            self.top+=1
            self.array.append(data)

    def pop(self):
        if self.isempty():
            print("Stack Underflow")
            return
        else:
            self.top -= 1    
            return self.array.pop()

    def print(self):

        if self.isempty(): 
            print("Empty stack ")
            return

        k = 0
        while k <=self.top:
            print(self.array[k],end=' ') 
            k+=1  
        print('\n')   


def insertatbottom(s,popped):
    if s.isempty():
        s.push(popped)
        return
    else:
        pop_ele = s.pop()  
        insertatbottom(s,popped)
        s.push(pop_ele)


def reversestack(s):
    if s.isempty(): 
        return

    popped = s.pop()
    reversestack(s)
    insertatbottom(s,popped)  



s = stack()
s.push(1)
s.push(2)
s.push(3)
s.print()

reversestack(s)
s.print()
  

