
## iterative approach

class node:
    def __init__(self,data):
        self.data = data
        self.next = None



def printlist(head):
        temp = head
        while(temp != None): 
            print(temp.data,end=" ")
            temp = temp.next    


head = node(1007)
temp = head
temp.next = node(5)
temp.next.next = node(17)
temp.next.next.next = node(27)
temp.next.next.next.next = node(7)
temp.next.next.next.next.next = node(1)

printlist(head)
print("")


