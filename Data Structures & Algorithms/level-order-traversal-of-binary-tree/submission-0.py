# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list1 = []
        count = 0
        
        def traverse(root,count):
            nonlocal list1
            if len(list1) == count and root:
                list1.append([])
            if root:    
                list1[count].append(root.val)
                
                traverse(root.left,count+1)
                traverse(root.right,count+1)
        traverse(root,count)    
        return list1    
        