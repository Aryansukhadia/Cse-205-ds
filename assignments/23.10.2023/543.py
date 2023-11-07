# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        def maxDepth(self, root):
            if root == None:
                return 0
            ld = self.maxDepth(root.left)
            if ld == -1:
                return -1
            rd = self.maxDepth(root.right)
            if rd == -1:
                return -1
            if abs(ld - rd) > 1:
                return -1
            return max(ld, rd) + 1
        def isBalanced(self, root):
            return self.maxDepth(root) != -1
    