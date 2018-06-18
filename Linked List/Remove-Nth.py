# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def lengthOf(self, l):
        if l is None:
            return 0
        else:
            count = 1
            while l.next is not None:
                l = l.next
                count += 1
            return count
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        k = self.lengthOf(head)
        if k == 0:
            return None
        if k == n:
            return head.next
        if n == 0:
            curr = head
            for i in range(k-1):
                curr = curr.next
            curr.next = None
            return head
        else:
            d = k-n
            curr = head
            for i in range(d-1):
                curr = curr.next
            succ = curr.next
            curr.next = succ.next
            return head
                
    