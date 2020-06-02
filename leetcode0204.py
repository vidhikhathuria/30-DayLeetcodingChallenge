# Problem Link : https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diameter(node, ans=1):
            if node == None:
                return 0, ans
            left, ans = diameter(node.left, ans)
            right, ans = diameter(node.right, ans)
            ans = max(left + right + 1, ans)
            return max(left, right) + 1, ans
        ans = 1
        _, ans = diameter(root)
        return ans - 1