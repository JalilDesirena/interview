import collections
from importlib.resources import contents
import queue


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

 
def connect(root:'Node')-> 'Node':
    if not root:
        return root
    
    q=collections.deque()
    q.append(root)
    while q:
        curr = q.popleft()
        #Case 1: two childrens
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next and curr.next.left:
                curr.right.next = curr.next.left
            elif curr.next and (not curr.next.left) and curr.next.right:
                curr.right.next = curr.next.right
            q.append(curr.left)
            q.append(curr.right)
        #Case 2: It has left children but not the right one
        elif curr.left and not curr.right:
            if curr.next and curr.next.left:
                curr.left.next = curr.next.left
            elif curr.next and not curr.next.left and curr.next.right:
                curr.left.next = curr.next.right
            q.append(curr.left)

        #Case 3: It has the right children but not the left one
        elif not curr.left and curr.right:
            if curr.next and curr.next.left:
                curr.right = curr.next.left
            elif curr.next and not curr.next.left and curr.next.right:
                curr.right = curr.next.right
            q.append(curr.right)
    return root


def connect2(root:'Node') -> 'Node':
    if not root:
        return root
    
    queue = contents.deque()
    queue.append(root)
    while queue:
        pre=None
        for n in range(len(queue)):
            cur = queue.popleft()
            if pre:
                pre.next = cur
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            pre=cur 
    return root               
