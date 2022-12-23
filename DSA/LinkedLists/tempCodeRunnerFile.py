

## iterative approach

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def reverseListRecursively(self,head):
        if head is None or head.next is None:
            return head

        node1 = self.reverseListRecursively(head.next)    ## this will return the last entry 
        head.next.next = head
        head.next = None

        return node1

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

llist.head = llist.reverseListRecursively(llist.head)
llist.printlist()


