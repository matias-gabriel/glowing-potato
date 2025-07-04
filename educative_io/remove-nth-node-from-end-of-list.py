# Definition for a singly linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode


def remove_nth_last_node(head: ListNode, n: int) -> ListNode:
    """
    Removes the nth node from the end of a singly linked list.

    This function utilizes a two-pointer approach to find and remove the desired
    node in a single pass. A 'right' pointer is first advanced `n` nodes into the
    list. Then, both a 'left' and 'right' pointer are advanced simultaneously
    until the 'right' pointer reaches the end of the list. At this point, the
    'left' pointer will be positioned just before the node that needs to be
    removed, allowing for its removal by updating the `next` reference.

    Args:
        head: The head of the linked list.
        n: The position from the end of the list of the node to remove (1-indexed).

    Returns:
        The head of the modified linked list.

    Edge Cases:
        - If `n` is equal to the length of the list, the head node is removed.

    Constraints:
        - The number of nodes in the list is `k`.
        - 1 <= k <= 10^3
        - -10^3 <= Node.value <= 10^3
        - 1 <= n <= k
    """
    left_pointer = head
    right_pointer = head

    # Advance the right_pointer n steps forward.
    current_n = 0
    while right_pointer.next:
        right_pointer = right_pointer.next
        current_n += 1

        if current_n == n:
            break

    # If the loop finishes before right_pointer has moved n steps,
    # it means n is equal to the length of the list.
    # Therefore, the head node must be removed.
    if current_n != n:
        return head.next

    # Move both pointers until the right_pointer reaches the end of the list.
    # The left_pointer will now be at the node just before the target node.
    while right_pointer.next:
        right_pointer = right_pointer.next
        left_pointer = left_pointer.next

    # Skip over the nth node from the end to remove it.
    removed_node = left_pointer.next
    left_pointer.next = removed_node.next

    return head
