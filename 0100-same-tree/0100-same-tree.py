# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if not is_same(p.left,q.left):
                return False
            if not is_same(p.right, q.right):
                return False

            return p.val == q.val

        return is_same(p,q)
                
        