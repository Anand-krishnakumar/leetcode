# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        else:
            currhead = head
            while head.next is not None:
                p = head.next
                head.next = p.next
                p.next = currhead
                currhead = p
            return currhead    
            
            
                