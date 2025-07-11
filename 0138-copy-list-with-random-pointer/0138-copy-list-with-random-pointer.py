"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if not head:
            return head
        node_copy_hash = {}
        traverse_head = head

        while traverse_head:
            node_copy_hash[traverse_head] = Node(traverse_head.val)
            traverse_head = traverse_head.next

        traverse_head = head
        while traverse_head:
            node_copy = node_copy_hash[traverse_head]
            node_next_copy =  node_copy_hash[traverse_head.next] if traverse_head.next is not None else None
            node_next_random =  node_copy_hash[traverse_head.random] if traverse_head.random is not None else None

            node_copy.next = node_next_copy
            node_copy.random = node_next_random

            traverse_head = traverse_head.next

        return node_copy_hash[head]
        