
## swap the start alternate k nodes


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
ll.head = ll.reverse(ll.head,4)  
ll.printlist()       



''' Another idea for reversing k alternate nodes in
def reverse(self,head,k):
        temp  = head
        for i in range(k):
            if temp == None: 
                print(" size greater than list size")
                return
            temp = temp.next

        temp = head
        ## since condition satisfies,lets reverse starting k nodes

        prev = None
        current = dummy = temp
        future = temp.next
        i =0
        while i<k and future:
            current.next = prev
            prev = current
            current = future
            future = future.next
            i+=1
        print(i)    

        if i==k-1:
            current.next = prev
            return current

        dummy.next =  current
        return prev   
'''