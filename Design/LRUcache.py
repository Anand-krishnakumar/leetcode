# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
class Node(object):
    def __init__(self, key = None, value = None):
        self. key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d.keys():
            node = self.d[key]
            self._remove(node)
            self._add(node)
            return node.value
            
        return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d.keys():
            self._remove(self.d[key])
        n = Node(key, value)
        self._add(n)
        self.d[key] = n
        if len(self.d) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.d[n.key]
        
    def _remove(self, node):
        #remove node
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
    
    def _add(self, node):
        #add node to end of the Doubly-linked list
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)