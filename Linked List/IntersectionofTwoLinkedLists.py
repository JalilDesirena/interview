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
node23.next = node2

head1 = node1
head2 = node2
visited = []
while head1:
    visited.append(tuple([head1,head1.val]))
    head1 = head1.next
while head2:
    cnode = tuple([head2,head2.val])
    if cnode in visited:
        print('INTESCTION IN:', head2.val)
    head2=head2.next

