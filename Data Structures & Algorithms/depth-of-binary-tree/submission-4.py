# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        height = 0
        def depth(node, h):
            if node == None: return
            nonlocal height
            height = max(height, h)

            depth(node.left, h + 1)
            depth(node.right, h + 1)
        
        depth(root, 1)

        return height