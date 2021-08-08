#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
from Tool.Python.TreeNode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = root.val
        def maxSubPathSum(node: TreeNode) -> int:
            nonlocal ans
            if node.left and node.right:
                max_left = maxSubPathSum(node.left)
                max_right = maxSubPathSum(node.right)
                ans = max(max_left, max_right, max_left + max_right + node.val, ans)
                return max(node.val, node.val + max(max_left, max_right))
            elif node.left:
                max_left = maxSubPathSum(node.left)
                ans = max(max_left, max_left + node.val, ans)
                return max(node.val, node.val + max_left)
            elif node.right:
                max_right = maxSubPathSum(node.right)
                ans = max(max_right, max_right + node.val, ans)
                return max(node.val, node.val + max_right)
            else:
                ans = max(node.val, ans)
                return node.val
        res = maxSubPathSum(root)
        ans = max(ans, res)
        return ans
        
# @lc code=end
# print(Solution().maxPathSum(TreeNode.build([-1,5,None,4,None,None,None,2,-4])))
# print(Solution().maxPathSum(TreeNode.build([-10,9,20,None,None,15,7])))
# print(Solution().maxPathSum(TreeNode.build([1,2,3])))
# print(Solution().maxPathSum(TreeNode.build([-1,5,None,4,None,None,2,-4])))
print(Solution().maxPathSum(TreeNode.build([-1])))

