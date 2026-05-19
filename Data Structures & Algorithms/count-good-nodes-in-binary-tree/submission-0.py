# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def traverse(node, upper):
            nonlocal count
            if node is None:
                return
            if node.val>=upper:
                count+=1

            traverse(node.left,max(upper,node.val))
            traverse(node.right,max(upper,node.val))    

        traverse(root,root.val)    
        return count