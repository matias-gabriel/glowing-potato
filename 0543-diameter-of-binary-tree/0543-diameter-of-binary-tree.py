# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def height(current_height, node, memo):
  if not node:
    return (0, 0)
  if node in memo:
    return memo[node]

  left_height, ldiameter = height(current_height + 1, node.left, memo)
  right_height, rdiamater  = height(current_height + 1, node.right, memo)
  diameter = left_height + right_height

  memo[node] =  (1 + max(left_height, right_height), max(diameter, ldiameter, rdiamater))

  return memo[node]



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      memo_heights = {}
      _, diameter = height(-1, root, memo_heights)

      return diameter
        