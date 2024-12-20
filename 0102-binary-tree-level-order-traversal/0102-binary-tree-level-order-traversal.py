# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append(root)
        res=[]
        while len(q):
            lev=[]
            for i in range(len(q)):
                ele=q.popleft()
                lev.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            res.append(lev)
        return res
        