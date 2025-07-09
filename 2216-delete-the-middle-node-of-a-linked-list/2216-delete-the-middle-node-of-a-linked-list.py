# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = None
        slow = head
        fast = head

        if not head.next:
            return None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow

        finder = head

        while finder.next and finder.next != middle:
            finder = finder.next

        finder.next = finder.next.next

        return head
