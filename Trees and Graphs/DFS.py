#Depth-First Search --- In Order and Post Order
#Stacks
"""
            1 
          /   \
        2       3
      /   \ 
    4       5
Depth First Traversals: 
(a) Inorder (Left, Root, Right) : 4 2 5 1 3 
(b) Preorder (Root, Left, Right) : 1 2 4 5 3 
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
"""



from inspect import stack
from itertools import tee

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def dfs_rec(tree):
    if tree is not None:
        #print(tree.val) #Preorder
        dfs_rec(tree.left)
        #print(tree.val) #Inorder
        dfs_rec(tree.right)
        print(tree.val) #Postorder
def dfs_iter(tree):
    stack=[]
    stack.append(tree)
    while len(stack) >0:
        node = stack.pop()
        if node is not None:
            print(node.val)
            stack.append(node.right)
            stack.append(node.left)

def dfs_rec2(tree):
  if tree is not None:
    print(tree.val)
    dfs_rec2(tree.left)
    dfs_rec2(tree.right)


root = TreeNode('1')
n1 = TreeNode('2')
n2 = TreeNode('3')
n3 = TreeNode('4')
n4 = TreeNode('5')
root.left=n1
root.right=n2
n1.left = n3
n1.right = n4

dfs_rec2(root)