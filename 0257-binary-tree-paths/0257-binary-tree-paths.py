# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


        
    def traverse(self,root,result,temp) :
        if not root :
            return 
        temp.append(root.val)
        if not root.right and not root.left :
            result.append(temp)
            temp = []
        k = []
        for i in temp:
            k.append(i)
        self.traverse(root.left,result,temp)
        self.traverse(root.right,result,k)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root :
            return []
        result = []
        temp = []
        self.traverse(root,result,temp)
        final = []
        for l in result :
            k = '->'.join(str(i) for i in l)
            final.append(k)            
        return final




        