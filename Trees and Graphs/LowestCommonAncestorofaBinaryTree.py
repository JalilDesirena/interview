from turtle import left, right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestcommonancestor(root,p,q):
    return helper(root, q,q)
def helper(node, p, q):
    if node is None:
        return node
    
    if node.val == p.val or node.val == q.val:
        return node
    
    left_subtree = helper(node.left,p,q)
    right_subtree = helper(node.right,p,q)

    if left_subtree is None:
        return right_subtree
    if right_subtree is None:
        return left_subtree
    return node
    
