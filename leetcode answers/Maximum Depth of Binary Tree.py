# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        INPUT: root of a binary tree
        OUTPUT: maximum depth
        SOLUTION:
        
        recursion
        
        retrieve left and right heights
        if left is greater return left
        otherwise return right
        
        '''
        if (root == None): return 0
        
        left_depth = self.maxDepth(root.left) + 1 
        right_depth = self.maxDepth(root.right) + 1
        
        return left_depth if left_depth > right_depth else right_depth
        