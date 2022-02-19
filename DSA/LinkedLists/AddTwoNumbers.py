

## given that the linked list 
## numbers ar stored in reverse order 
## return their sum in reverse order


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

    def reverselist(self,head):
        prev = None
        while head:
            future  = head.next
            prev = head
            head.next = prev
            head = future
        return prev     
    
    def addTwoNumbers(self,l1,l2):
        
   
        num1 = num2 = 0
        head1 = self.reverselist(l1)
        head2 = self.reverselist(l2)
        
        while head1:
            num1 = num1*10 + head1.data
            head1 = head1.next
            
        while head2:
            num2 = num2*10 + head2.data
            head2 = head2.next
            
        result = num1 + num2
        
        ans_head = self.head
        
        while result:
            ans_head.data = int(result//10)
            ans_head = ans_head.next
            result = int(result//10)
        ans_head.next = None
        
  
    def printlist(self):
        if self.head==None:
            return
        temp = self.head
        while(temp != None): 
            print(temp.data,end=" ")
            temp = temp.next



l1 = llist()
l1.push(3)
l1.push(4)
l1.push(2)

l2 = llist()

l2.push(4)
l2.push(6)
l2.push(5)

l3 = llist()
l3.addTwoNumbers(l1.head,l2.head)
l3.printlist()
