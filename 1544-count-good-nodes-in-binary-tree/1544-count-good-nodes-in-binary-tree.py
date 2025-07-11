# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGoodNodes(self, node, currentCount, maxNode):
      newCount = 0
      newMaxNode = maxNode

      if not node:
        return 0

      if node.val >= maxNode:
        newCount+=1
        newMaxNode = node.val


      return self.countGoodNodes(node.left, currentCount, newMaxNode) + self.countGoodNodes(node.right, currentCount, newMaxNode) + newCount



    def goodNodes(self, root: TreeNode) -> int:
      return self.countGoodNodes(root, 0, root.val)
        