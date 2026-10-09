# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse the linked list with a node (which is our pointer)
        # we also keep another pointer at the previous node on the original linked list
        if not head:
            return head
        prev = None
        while head:
            node = head
            head = head.next
            node.next = prev
            prev = node

        return node


        