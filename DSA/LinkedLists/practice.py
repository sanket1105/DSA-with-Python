


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

    def append(self,new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return

        temp =  self.head
        while(temp.next):
            temp = temp.next

        temp.next = new_node          

    def merged(self,head1,head2):
        temp1 = head1
        temp2 = head2

        while temp1 and temp2:
            if temp1.data < temp2.data:
                self.append(temp1.data)
                temp1 = temp1.next 
            else: 
                self.append(temp2.data)    
                temp2 = temp2.next

        while temp1:
            self.append(temp1.data)
            temp1 = temp1.next

        while temp2:
            self.append(temp2.data)
            temp2 = temp2.next             

    def printlist(self):
        if self.head==None:
            return
        temp = self.head
        while(temp != None): 
            print(temp.data,end=" ")
            temp = temp.next



ll1 = llist()
ll1.push(4)
ll1.push(2)
ll1.push(1)

ll2 = llist()

ll2.push(4)
ll2.push(3)
ll2.push(1)

ll3 = llist()
ll1.printlist()
print("")
ll2.printlist()
print("")
ll3.merged(ll1.head,ll2.head)
ll3.printlist()

               

