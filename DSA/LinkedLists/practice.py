


class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self,data):
        newnode  = node(data)
        newnode.next = self.head
        self.head = newnode


    def insertafter(self,prev,data):
        newnode = node(data)

        if prev==None:
            print("previous link doesnt exists")
            return
        temp = prev.next
        prev.next = newnode
        newnode.next = temp


    def append(self,data):
        newnode = node(data)
        if self.head==None:
            self.head = newnode
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode  


    def delnode(self,key):
        if self.head is not None:
            if self.head.data == key:
                self.head = self.head.next
                return

        temp = self.head    
        while temp is not None:  
            while temp.data != key:
                prev = temp
                temp = temp.next

        if temp==None: return
        prev.next =temp.next       

    def deletelist(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end= " ")    
            temp = temp.next

#####################################################################################            

if __name__ == '__main__':

    llist = linkedlist()
    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third

    llist.printlist()

    print("####################################")
    ## adding a new head to link list

    llist.push(14)
    llist.printlist()

    print("####################################")
    llist.insertafter(llist.head,15)
    llist.printlist()

    print("####################################")
    llist.append(16)
    llist.printlist()

    print("####################################")

    ## lets build the new list 
    llist2 = linkedlist()
    llist2.append(6)
    llist2.push(7)
    llist2.push(1)
    llist2.append(4)
    llist2.insertafter(llist2.head.next,8)
    llist2.printlist()

    llist2.delnode(7)
    llist2.printlist()

    llist2.delAtPos(4)
    llist2.printlist()

    llist2.deletelist()
    print("linked list deleted")


