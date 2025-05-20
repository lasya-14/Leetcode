# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count=[]
        if not root:
            return 0
        q=deque()
        q.append(root)
        while q:
            same_level=[]
            for i in range(len(q)):
                node=q.popleft()
                same_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count.append(same_level)
            
        return len(count)
        