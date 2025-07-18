# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = None
        head=None
        heap = []
        memory = {}

        for idx, k in enumerate(lists):
            l_node = k
            if l_node:
                heapq.heappush(heap, (l_node.val, idx))
                memory[idx] = l_node

        while heap:
            val, idx = heapq.heappop(heap)
            l_node = memory[idx]
            print(idx)
            if not node:
                node = l_node
                head = l_node
            else:
                node.next = l_node
                node = node.next

            # push next element

            if l_node.next:
                new_node = l_node.next
                memory[idx] = new_node
                heapq.heappush(heap, (new_node.val, idx))

        return head




        