# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        highest = float("inf")
        lowest = float("-inf")
        def check(highest,lowest,root):
            if not root:
                return True
            if not root.val < highest or not root.val > lowest:
                return False
            return check(root.val,lowest,root.left) and check(highest,root.val,root.right)
        return check(highest,lowest,root)    