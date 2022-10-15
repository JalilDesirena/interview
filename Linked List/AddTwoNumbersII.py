# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reverseList(head: ListNode) -> ListNode:
    last = None
    while head:
        # keep the next node
        tmp = head.next
        # reverse the link
        head.next = last
        # update the last node and the current node
        last = head
        head = tmp
    
    return last

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # reverse lists
    l1 = reverseList(l1)
    l2 = reverseList(l2)
    
    head = None
    carry = 0
    while l1 or l2:
        # get the current values 
        x1 = l1.val if l1 else 0
        x2 = l2.val if l2 else 0
        
        # current sum and carry
        val = (carry + x1 + x2) % 10
        carry = (carry + x1 + x2) // 10
        
        # update the result: add to front
        curr = ListNode(val)
        curr.next = head
        head = curr
        
        # move to the next elements in the lists
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        curr = ListNode(carry)
        curr.next = head
        head = curr

    return head

node_1= ListNode(val=1)
node_2= ListNode(val=2)
node_3= ListNode(val=3)
node_12= ListNode(val=4)
node_22= ListNode(val=5)
node_23= ListNode(val=6)
#node_7= ListNode(val=7)
node_1.next=node_2
node_2.next=node_3
node_3.next=None
node_12.next=node_22
node_22.next=node_23
node_23.next=None

result=addTwoNumbers(l1=node_1,l2=node_12)