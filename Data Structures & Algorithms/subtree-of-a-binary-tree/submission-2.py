# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(node,subRoot):
            if not node and not subRoot:
                return True
            if node and not subRoot:
                return False
            if subRoot and not node:
                return False
            if node.val != subRoot.val:
                return False
            if not isSameTree(node.left,subRoot.left):
                return False
            if not isSameTree(node.right,subRoot.right):
                return False
            return True 

        if root is None:
            return False
        if subRoot is None:
            return True    
        if root.val == subRoot.val:
            if isSameTree(root,subRoot):
                return True
            if self.isSubtree(root.left,  subRoot): 
                return True
            if self.isSubtree(root.right, subRoot):
                return True    
        if self.isSubtree(root.left,subRoot):
            return True
        if self.isSubtree(root.right,subRoot):
            return True
            
        return False                
           