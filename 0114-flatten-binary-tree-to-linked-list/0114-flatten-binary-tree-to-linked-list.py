# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traversal(node, memo):
    if not node:
      return
    memo.append(node)
    if node.left:
      traversal(node.left, memo)
    if node.right:
      traversal(node.right, memo)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        memo = []
        traversal(root,memo)

        prev = None

        while len(memo):
          last = memo.pop()

          last.right = prev
          last.left = None

          prev = last

        