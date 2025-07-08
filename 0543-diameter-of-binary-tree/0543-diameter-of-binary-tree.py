# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def height(current_height, node, memo):
  if not node:
    return 0
  if node in memo:
    return memo[node]

  memo[node] =  1 + max(height(current_height + 1, node.left, memo), height(current_height + 1, node.right, memo))

  return memo[node]

def get_max_diameter(root, memo_heights):
  if not root:
    return 0

  calc_result = memo_heights[root.left] if root.left else 0
  calc_result = calc_result + memo_heights[root.right] if root.right else  calc_result
  return max(
    calc_result,
    get_max_diameter(root.left, memo_heights),
    get_max_diameter(root.right, memo_heights),
  )

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      memo_heights = {}
      height(-1, root, memo_heights)

      return get_max_diameter(root, memo_heights)
        