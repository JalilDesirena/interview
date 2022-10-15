# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Evaluate if p and q are lesser or greater that the parent



def lowestCommonAncestor(root,p,q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    # Value of current node or parent node.
    parent_val = root.val

    # Value of p
    p_val = p.val

    # Value of q
    q_val = q.val

    # If both p and q are greater than parent
    if p_val > parent_val and q_val > parent_val:    
        return lowestCommonAncestor(root.right, p, q)
    # If both p and q are lesser than parent
    elif p_val < parent_val and q_val < parent_val:    
        return lowestCommonAncestor(root.left, p, q)
    # We have found the split point, i.e. the LCA node.
    else:
        return root