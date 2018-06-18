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
            
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        a = self.lengthOf(headA)
        b = self.lengthOf(headB)
        if a >= b:
            d = a - b
            if d > 0:
                for i in range(d):
                    p1 = p1.next
        else:
            d = b - a
            for i in range(d):
                p2 = p2.next
        while p1 is not None and p2 is not None:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
        
    
        