# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast_pointer = head
        normal_pointer = head

        while fast_pointer and fast_pointer.next:
            normal_pointer = normal_pointer.next
            fast_pointer = fast_pointer.next.next

        palindrome_pointer = head

        reverted_normal_pointer = None
        prev = None

        while normal_pointer:
            aux = normal_pointer
            normal_pointer = normal_pointer.next
            aux.next = prev
            prev = aux

        reverted_normal_pointer = prev
        while reverted_normal_pointer:
            if reverted_normal_pointer.val != palindrome_pointer.val:
                return False

            reverted_normal_pointer = reverted_normal_pointer.next
            palindrome_pointer = palindrome_pointer.next

        return True
