import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root:'Node') -> 'Node':
    if not root:
        return root
    
    q = collections.deque()
    q.append(root)
    while q:
        curr = q.popleft()
        if curr.left and curr.right: # Check if has childs
            curr.left.next = curr.right # link the right child with the left
            if curr.next: #If the node already has a next
                curr.right.next = curr.next.left #Link the right child of one node with the left of the other one
            q.append(curr.left)
            q.append(curr.right)
        else:
            break
    return root




