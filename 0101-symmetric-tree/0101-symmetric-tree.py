# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        def check(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)

        return check(root.left, root.right)