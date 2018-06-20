# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head.val == val:
            head = head.next
            if head is None:
                return None
        prev = head
        curr = head.next
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = prev.next
                curr = curr.next
        return head
