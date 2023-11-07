# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            leftmax = dfs(root.left)
            leftmax = max(leftmax,0)
            rightmax = dfs(root.right)
            rightmax = max(rightmax,0)

            res[0] = max(res[0], root.val + rightmax + leftmax)
            return root.val + max(leftmax,rightmax)
        dfs(root)
        return res[0]

        