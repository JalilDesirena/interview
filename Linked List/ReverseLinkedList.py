from os import preadv


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node_1= ListNode(val=1)
node_2= ListNode(val=2)
node_3= ListNode(val=3)
node_4= ListNode(val=4)
node_5= ListNode(val=5)
node_6= ListNode(val=6)

node_1.next=node_2
node_2.next=node_3
node_3.next=node_4
node_4.next=node_5
node_5.next=node_6

ListNode(1,2)
ListNode(3)

def reverseList(head):
    
    prev = None
    node = head
    
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    return prev

reverseList(node_1)

def reverst2(head):
    preav=None
    curr=head
    while curr:
        temp=curr.next
        curr.next=preav
        preav=curr
        curr=temp
    return preav