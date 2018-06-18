# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        a = head
        b = head
        while b.next is not None and b.next.next is not None:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False
                