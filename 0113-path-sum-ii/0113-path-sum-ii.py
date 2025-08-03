# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        initial_path = []
        final_results = []
        def get_count(node, target, path, results):
            if not node:
                return
            if target == 0 and not node.left and not node.right:
                results.append(path[:])
                return 
            if node.left:
                path.append(node.left.val)
                get_count(node.left, target - node.left.val, path, results)
                path.pop()

            if node.right:
                path.append(node.right.val)
                get_count(node.right, target - node.right.val, path, results)
                path.pop()

        if not root:
            return []

        get_count(root, targetSum - root.val, [root.val], final_results)
        return final_results

            
        
