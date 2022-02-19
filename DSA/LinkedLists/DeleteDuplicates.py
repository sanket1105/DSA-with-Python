

## given that the linked list is in sorted form


class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class llist:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        if self.head==None:
            self.head = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node

    def deleteDuplicates(self):
        if self.head == None:
            return self.head
        temp = self.head
        while temp.next !=None:  
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return self.head        

    def printlist(self):
        if self.head==None:
            return
        temp = self.head
        while(temp != None): 
            print(temp.data,end=" ")
            temp = temp.next



ll = llist()
ll.push(7)
ll.push(7)
ll.push(5)
ll.push(3)
ll.push(1)
ll.push(1)
ll.printlist()
print("")
ll.deleteDuplicates()   
ll.printlist()                 

