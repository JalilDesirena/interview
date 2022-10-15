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
#node_7= ListNode(val=7)
node_1.next=node_2
node_2.next=node_3
node_3.next=node_4
node_4.next=node_5
node_5.next=node_6
node_6.next=node_4

def likendlist_cycle(head):
    curr=head
    visited=[]
    while curr:
        visiting=tuple([curr, curr.val])
        if visiting in visited:
            return True
        visited.append(visiting)
        #print(curr.val, curr.next.val)
        curr=curr.next
    return False


r=likendlist_cycle(node_1)
print(r)