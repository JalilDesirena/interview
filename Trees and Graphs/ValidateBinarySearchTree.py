# Definition for a binary tree node.



class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isValidBST(root) -> bool:
    return validate(root)
        
def validate(root, low=-2**33, high=2**33) -> bool:
    if root is None:
        return True
    if root.val <= low or root.val >= high:
        print(low)
        print(high)
        print(root.val)
        return False
    
    return validate(root.left, low, root.val) and validate(root.right, root.val, high)


                #15
             #9      #25
         #8    13   7    122
                 
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


result = isValidBST(root)
print(result)
