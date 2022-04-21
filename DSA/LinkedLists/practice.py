

## iterative approach

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def reverseiterative(self,head):

        if head == None or head.next == None: return

        prev = None
        present = head
        future = head.next

        while future.next:
            present.next = prev
            prev = present
            present = future
            future = future.next
        present.next = prev
        future.next = present

        return future     ## head     

    def push(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while(temp != None): 
            print(temp.data,end=" ")
            temp = temp.next    



llist = Linkedlist()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

llist.printlist()
print("")

llist.head = llist.reverseiterative(llist.head)
llist.printlist()


