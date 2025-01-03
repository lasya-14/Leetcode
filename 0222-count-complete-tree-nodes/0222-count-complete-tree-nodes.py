# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        li=[]
        count=0
        def inorder(root):
            if root:
                inorder(root.left)
                li.append(root.val)
                inorder(root.right)
        inorder(root)
        for i in li:
            count+=1
        return count
        