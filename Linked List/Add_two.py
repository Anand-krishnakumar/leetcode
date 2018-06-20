# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        if head is None:
            return None
        currhead = head
        while head.next is not None:
            prev = head.next
            head.next = prev.next
            prev.next = currhead
            currhead = prev
        return currhead
    def getNumber(self, head):
        num = 0
        if head is None:
            return num
        while head is not None:
            num = num*10 + head.val
            head = head.next
        return num
    def makeList(self, num): 
        node = ListNode(-1)
        curr = node
        if num == 0:
            return ListNode(0)
        while num>0:
            l = num%10
            num = num/10
            new = ListNode(l)
            curr.next = new
            curr = curr.next
        return node.next
            
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        k1 = self.reverse(l1)
        k2 = self.reverse(l2)
        t = self.getNumber(k1) + self.getNumber(k2)
        return self.makeList(t)
        
            
                
                
        
        