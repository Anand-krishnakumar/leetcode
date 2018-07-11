# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
       
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        stack = []
        stack.append(root)
        s = ''
        while len(stack) > 0:
            node = stack.pop()
            s += str(node.val) +' '
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return s[:len(s)-1]
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pre  = [int(i) for i in data.split()]
        inorder = sorted(pre)
        return self.makeTree(pre, inorder)
    def makeTree(self, pre, inorder):
        if inorder:
            root = TreeNode(pre.pop(0))
            k = inorder.index(root.val)
            root.left = self.makeTree(pre, inorder[0:k])
            root.right = self.makeTree(pre, inorder[k+1:])
            return root          
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))