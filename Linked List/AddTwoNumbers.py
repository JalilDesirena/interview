from tkinter.messagebox import NO


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


def addTwoNumbers(l1, l2):
    result = ListNode(0) # Create a new node for the result
    result_tail = result
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2+carry, 10)
        out = val1+val2+carry // 10
        carry = val1+val2+carry % 10 
        result_tail.next = ListNode(out)
        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
    return result.next

a = addTwoNumbers(node_1, node_12)