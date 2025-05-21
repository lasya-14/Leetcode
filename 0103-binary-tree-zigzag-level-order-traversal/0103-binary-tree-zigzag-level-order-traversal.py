# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=deque()
        q.append(root)
        left_to_right=True
        while q:
            sample_level=[]
            for i in range(len(q)):
                node=q.popleft()
                sample_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                sample_level.reverse()
            res.append(sample_level)
            left_to_right = not left_to_right
        return res
        