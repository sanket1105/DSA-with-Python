
## linked list won't be continous memory allocation
## every single box is known as a node 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None    

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertafter(self,prev,new_data):
        if prev == None:
            print("Previous node must be a linked list node \n")
        new_node = Node(new_data)
        new_node.next = prev.next
        prev.next = new_node   

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        temp =  self.head
        while(temp.next):
            temp = temp.next

        temp.next = new_node      


    def delnode(self,key):
        temp = self.head
        if temp is not None: ## if head has the key value
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        ## if key not found: temp will go till the end and will take tails next value that is None
        if temp==None: return

        prev.next = temp.next
        temp = None


    def delAtPos(self,pos):
        temp = self.head

        if pos==0:
            if temp==None: return
            else: 
                self.head = temp.next
                temp = None
                return

        for i in range(0,pos):
            prev = temp
            temp = temp.next

            if temp==None:    
                print("Pos greater than linked list length \n")
                return

        prev.next = temp.next
        temp = None    

    def deletelist(self):
        ## its just a shortcut to delete a list
        ## self.head = None    

        curr = self.head
        while curr:
            prev = curr.next
            del curr.data
            curr=prev   


    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        print("")    




if __name__ == '__main__':

    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

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

    