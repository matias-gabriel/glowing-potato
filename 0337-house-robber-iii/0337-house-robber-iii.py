# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
      def r(node, memo):
        if not node:
          return 0

        if node in memo:
          return memo[node]

        node_left_right = r(node.left.right, memo) if node.left else 0
        node_left_left = r(node.left.left, memo) if node.left else 0
        node_right_right = r(node.right.right, memo) if node.right else 0
        node_right_left = r(node.right.left, memo) if node.right else 0
        result =  max(
          node.val + node_left_right + node_left_left + node_right_right + node_right_left,
          r(node.left, memo) + r(node.right, memo),
        )

        memo[node] = result
        return result

      return r(root,{})
        