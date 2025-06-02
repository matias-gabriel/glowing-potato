# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def removeItem(self, parent, item):
        parent.next = item.next if item else None

    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        start = 0
        new_head = head
        finder_node = None
        finder_node_parent = None

        # 1  

        if head.next == None:
            return head.next
        

        while new_head != None:
            start += 1
            if start >= n:
                if finder_node == None:
                    finder_node = head
                else:
                    finder_node_parent = finder_node
                    finder_node = finder_node.next
            new_head = new_head.next

        if finder_node_parent == None:
            head = head.next
        else:
            self.removeItem(finder_node_parent or head, finder_node)
        return head
        