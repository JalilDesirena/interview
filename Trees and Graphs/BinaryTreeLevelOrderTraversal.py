import collections


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def levelOrder(root):
    
    levels = []
    traversal(root, 0)
    return levels

def traversal(node, level):
    if node:
        if len(levels) <= level:
            levels += [[node.val]]
        else:
            levels[level] += [node.val]
        traversal(node.left, level+1)
        traversal(node.right, level+1)
        
from collections import deque

def levelOrder_iter(root) -> list[list[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
                 #15
             #9      #25
         #8    13   17    122
                 
root = TreeNode(val=15)
nodeI1 = TreeNode(val=9)
nodeD1 = TreeNode(val=25)
nodeI2 = TreeNode(val=8)
nodeD2 = TreeNode(val=13)
nodeI3 = TreeNode(val=17)
nodeD3 = TreeNode(val=122)

root.left = nodeI1
root.right = nodeD1
nodeI1.left = nodeI2
nodeI1.right = nodeD2
nodeD1.left = nodeI3
nodeD1.right = nodeD3

print(levelOrder_iter(root))