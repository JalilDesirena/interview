class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorderTraversal(root) -> list[int]:
    output = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            print(root.val)
            root = root.left
        else:
            holder = stack.pop()
            print(holder.val)
            output.append(holder.val)
            print(output)
            root = holder.right
    return output
    

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

result = inorderTraversal(root)
print(result)