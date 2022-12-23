
class node:
    def __init__(self,data):
        self.data = data
        self.next = None


def merge_function(head):
        if not head or not head.next: 
            return head

        mid  = getmid(head)
        head2 = mid.next
        mid.next = None
        l = merge_function(head)
        r = merge_function(head2)

        return mergesort(l,r)


def mergesort(head1,head2):
        merge = node(-1)  ## dummy node
        temp = merge

        while head1 and head2:
            if head1.data < head2.data:
                temp.next = head1
                head1 = head1.next

            else: 
                temp.next = head2
                head2 = head2.next 
            temp = temp.next

        if head1 == None: 
            temp.next  = head2
        else: 
            temp.next = head1         

        return merge.next         


def getmid(head):
            fast =head.next
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow                 

def printlist(head):
        
        temp = head
        while(temp != None): 
            print(temp.data,end=" ")
            temp = temp.next    


head = node(1007)
temp = head
temp.next = node(5)
temp.next.next = node(17)
temp.next.next.next = node(27)
temp.next.next.next.next = node(7)
temp.next.next.next.next.next = node(1)

printlist(head)
print("")
head1 = merge_function(head)
printlist(head1)



