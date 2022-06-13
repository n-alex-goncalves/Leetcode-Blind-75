# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None: return False
        if root.val == subRoot.val and self.isEqual(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isEqual(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (root1 == None and root2 == None): return True
        if (root1 == None or root2 == None): return False
        if (root1.val != root2.val): return False
        return self.isEqual(root1.left, root2.left) and self.isEqual(root1.right, root2.right)