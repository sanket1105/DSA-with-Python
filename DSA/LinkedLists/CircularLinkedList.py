

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circularlll():
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node = node(data)
        temp = self.head
        new_node.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node

        self.head = new_node


    def deletekey(self,key):
        if self.head == None: return

        temp = self.head

        if self.head.data == key:
            self.head = self.head.next

        while True:
            last = temp
            temp = temp.next
            if temp.data==key:
                last.next = temp.next
                del temp
                return

    def printlist(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data,end=" ")
                temp = temp.next
                if temp==self.head: break


cll = Circularlll()
cll.push(12)
cll.push(13)
cll.push(14)
cll.push(15)
cll.printlist()
print("")
cll.deletekey(12)
cll.printlist()