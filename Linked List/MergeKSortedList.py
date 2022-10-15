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






def mergeKLists(lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodes = []
        head = point = ListNode(0)
        #for each linkedlist get the nodes and append them into a list
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes): # Sort the list and create a node for each element to create a linked list
            point.next = ListNode(x)
            point = point.next
        return head.next

r = mergeKLists([node1, node21])
