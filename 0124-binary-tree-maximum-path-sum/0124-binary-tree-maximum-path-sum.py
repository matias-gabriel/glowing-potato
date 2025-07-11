# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calc_max_path_sum(self, node):
        if not node:
            return (0, 0)

        # return a tuple
        # the first position is the max value
        # traversing only by the left or by the right
        # the second position is max_path_sum of this subtree

        result_left = self.calc_max_path_sum(node.left)
        result_right = self.calc_max_path_sum(node.right)

        current_path = (
            max(node.val, node.val + max(result_left[0], result_right[0]))
            if (node.left and node.right)
            else max(node.val + result_left[0] + result_right[0], node.val)
        )

        current_sum = [
            node.val,
            node.val + result_left[0] + result_right[0],
            node.val + result_left[0],
            node.val + result_right[0],
        ]
        if node.left:
            current_sum.append(result_left[1])
        if node.right:
            current_sum.append(result_right[1])

        return (current_path, max(current_sum))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.calc_max_path_sum(root)[1]
