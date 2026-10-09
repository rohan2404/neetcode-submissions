# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 9
        # 5 6 7
        # 1 <= 5 so we start off with 1. 
        # 2 <= 5 so we have 1 -> 2
        # 9 > 5 so we have our next set to rnode and then rnode is bumped up one

        lnode, rnode = list1, list2
        head = ListNode()
        root = head
        while lnode and rnode:
            if lnode.val <= rnode.val:
                head.next = lnode
                lnode = lnode.next
            else:
                head.next = rnode
                rnode = rnode.next
            head = head.next
        while rnode:
            head.next = rnode
            rnode = rnode.next
            head = head.next
        while lnode:
            head.next = lnode
            lnode = lnode.next
            head = head.next

        return root.next

        