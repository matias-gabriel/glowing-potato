# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(level, node_left, node_right):
            if not node_left or not node_right: return

            if (level) % 2 == 0:
                aux = node_left.val
                node_left.val = node_right.val
                node_right.val = aux

            invert(level+1, node_left.left, node_right.right)
            invert(level+1, node_left.right, node_right.left)


        invert(0, root.left, root.right)
        return root

            
        