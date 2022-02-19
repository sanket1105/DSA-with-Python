
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doublyll:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        new_node.next = self.head

        if self.head is not None: 
            self.head.prev = new_node

        self.head = new_node

    def append(self,data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head    

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insertAfter(self,node1,data):
        new_node = node(data)

        if self.head is None:
            print("\n node to be inerted after must be node")  
            return

        temp = self.head
        while(temp is not node1):
            temp = temp.next

        if temp==None:
            print("\n Given node not found in the linked list, so can't be inserted")
            return    

        new_node.next = temp.next
        if temp.next is not None: temp.next.prev = new_node
        new_node.prev = temp
        temp.next = new_node


    def deletenode(self,node1):

        if self.head is None or node1 is None:
            print("\n Can't delete as the list is NULL")  
            return

        if self.head==node1:
            self.head= node1.next
            
        if node1.next is not None:
            node1.next.prev = node1.prev

        if node1.prev is not None: 
           node1.prev.next = node1.next

    def reverse(self):
        temp = None
        current = self.head
 
        # Swap next and prev for all nodes of
        # doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
 
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev


    def printList(self, node):
        while(node is not None):
            print(node.data,end=' ')
            node = node.next                      


if __name__ =='__main__':

    dll = doublyll()
    dll.append(6)
    dll.push(7)
    dll.push(1)
    dll.append(4)
    dll.insertAfter(dll.head.next,8)
    dll.printList(dll.head)
    print("")
    dll.deletenode(dll.head)
    dll.printList(dll.head)

    dll.reverse()
    print("")
    dll.printList(dll.head)
   

    

    


