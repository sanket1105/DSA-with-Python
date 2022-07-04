



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

    def reverse(self,head,k):
        temp = head
        for i in range(0,k):
            if temp==None:
                return head
            temp = temp.next
        ## reverse firt k if length > k
        prev = None
        curr = head
        
        for i in range(0,k):
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future

        if head!= None:
            head.next = curr

        count = 0
        while count<k-1 and curr:
            curr = curr.next
            count+=1   

        if curr:
            curr.next = self.reverse(curr.next,k)
        return prev

    def printlist(self):
        if self.head==None:
            return
        temp = self.head
        while(temp != None): 
            print(temp.data,end=" ")
            temp = temp.next    

ll = llist()
ll.push(4)
ll.push(7)
ll.push(5)
ll.push(3)
ll.push(1)
ll.push(8)
ll.printlist()
print("")
ll.head = ll.reverse(ll.head,5)  
ll.printlist()              