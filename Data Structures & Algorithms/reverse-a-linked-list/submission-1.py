# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node, current_node = None, head

        #      | new_head
        # a -> b
        # | previous_node

        # new_head = head.next
        # previous_node = head
        # previous_node.next = new_head
        # head = new_head
        # head.next = previous_node

        if head is None:
            return head

        while current_node:
            new_head = current_node.next
            
            current_node.next = previous_node
            previous_node = current_node

            current_node = new_head

        return previous_node