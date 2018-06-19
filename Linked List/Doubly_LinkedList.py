class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1
        k = self.head
        for i in range(index):
            k = k.next
        return k.val
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        new = Node(val)
        curr = self.head
        if curr is None:
            self.head = new
            self.size += 1
        else:
            while curr.next is not None:
                curr = curr.next 
            curr.next = new
            new.prev = curr
            self.size += 1

        
            
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if  index < 0 or index > self.size:
            return -1
        if index == self.size:
            self.addAtTail(val)
        else:
            node = Node(val)
            curr = self.head
            for i in range(index):
                curr = curr.next
            prev = curr.prev
            prev.next = node
            node.prev = prev
            node.next = curr
            curr.prev = node
            self.size += 1
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return
        curr = self.head
        if index == 0:
            self.head = curr.next
            self.size -= 1
        else:
            for i in range(index):
                curr = curr.next
            if curr is None:
                return 
            else:
                prev = curr.prev
                prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = prev
                elif curr.next is None:
                    curr.prev.next = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
            self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)