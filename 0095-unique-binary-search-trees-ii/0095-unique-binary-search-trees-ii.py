# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def fun(l,r):
            if l==r:
                return [None]
            op=[]
            for i in range(l,r):
                for lc in fun(l,i):
                    for rc in fun(i+1,r):
                        node=TreeNode(i+1)
                        node.left=lc
                        node.right=rc
                        op.append(node)
            return op
        return fun(0,n) if n>0 else []
        