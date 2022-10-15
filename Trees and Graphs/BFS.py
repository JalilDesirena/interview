#Quea
import queue
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bfs(node):
    q = deque()
    q.append(node)
    while len(q) > 0:
        node = q.popleft()
        if node is not None:
            print(node.val)
            q.append(node.left)
            q.append(node.right)

root = TreeNode('1')
n1 = TreeNode('2')
n2 = TreeNode('3')
n3 = TreeNode('4')
n4 = TreeNode('5')
root.left=n1
root.right=n2
n1.left = n3
n1.right = n4

bfs(root)