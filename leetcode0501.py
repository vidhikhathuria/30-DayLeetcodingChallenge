# Problem Link : https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def pathsum(node, maxm):
            if node == None:
                return 0, maxm
            l , maxm = pathsum(node.left, maxm)
            r, maxm = pathsum(node.right, maxm)
            left = max(0, l)
            right = max(0, r)
            maxm = max(left + right + node.val, maxm)
            return max(left, right) + node.val, maxm
        
        m = float('-inf')
        _, m = pathsum(root, m)
        return m