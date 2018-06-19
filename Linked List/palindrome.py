# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        else:
            currhead = head
            while head.next is not None:
                temp = head.next
                head.next = temp.next
                temp.next = currhead
                currhead = temp
            return currhead
    def mid(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        k1 = self.mid(head)
        k2 = self.reverse(k1)
        
        while head is not None and k2 is not None:
            if head.val != k2.val:
                return False
            head = head.next
            k2 = k2.next
        return True
                
            
        
        
        