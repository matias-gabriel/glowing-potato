
# 9 9 9 9 9
# 9 9 9 9 9 
# 8 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev_head = ListNode(0, None)
        node = prev_head
        residual = 0
        while l1 or l2 or residual:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            new_value = l1_value + l2_value + residual

            if new_value >= 10:
                residual = int(str(new_value)[0])
                new_value = int(str(new_value)[1])
            else:
                residual = 0

            node.next =  ListNode(new_value, None)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return prev_head.next




        
        