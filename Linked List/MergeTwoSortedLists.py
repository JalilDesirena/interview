from platform import node
from unittest import result


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(val=1)
node2 = ListNode(val=2)
node3 = ListNode(val=4)
node1.next = node2
node2.next = node3
node3.next = None

node21 = ListNode(val=1)
node22 = ListNode(val=3)
node23 = ListNode(val=4)
node21.next = node22
node22.next = node23
node23.next = None

head1 = node1
head2 = node21
head_r = None
temp=None
temp2=None

head_result = ListNode()
curr = head_result

while head1 and head2:
    if head1.val <= head2.val:
        curr.next = head1
        head1 = head1.next
    else:
        curr.next = head2
        head2=head2.next
    curr=curr.next
    val_curr = curr.val
    print(val_curr)

curr.next = head1 if head1 is not None else head2
#retuen head_result.next


