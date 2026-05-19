# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        list1 = []
        count = 0
        def traverse(root, count):
            if not root:
                return
            if root and len(list1) == count:
                list1.append(root.val)
                
            if root.right:
                traverse(root.right,count+1)
                    
            traverse(root.left, count+1)
        traverse(root,count)        
        return list1                
        