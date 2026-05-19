# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node is None:
                return 0
            leftHeight = dfs(node.left)
            if leftHeight == -1:
                return -1 
            rightHeight = dfs(node.right)
            if rightHeight == -1:
                return -1 

            if leftHeight> rightHeight and leftHeight - rightHeight >=2:
                return -1
            if leftHeight< rightHeight and rightHeight - leftHeight >=2:  
                return -1
            return 1 + max(leftHeight, rightHeight) 
        return dfs(root) != -1         
                            

        