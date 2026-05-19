# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def traverse(root):
            nonlocal count
            if root is None:
                return None
            leftval = traverse(root.left)
            if leftval is not None:
                return leftval
            count+=1
            if count == k:
                return root.val
            return traverse(root.right)
        return traverse(root)