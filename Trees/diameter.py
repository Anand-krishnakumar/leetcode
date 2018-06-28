# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepth(node):
            if node is None:
                return 0
            else:
                return 1 + max(maxDepth(node.left), maxDepth(node.right))
        def maxNodeLength(node):
            if node is None:
                return 0
            if node.left and node.right:
                return maxDepth(node.left) + maxDepth(node.right)
            elif node.left:
                return maxDepth(node.left)
            elif node.right:
                return maxDepth(node.right)
            else:
                return 0
        if root is None:
            return 0
        stack = []
        stack.append(root)
        _max = 0
        while len(stack) > 0:
            node = stack.pop()
            k = maxNodeLength(node)
        
            if k > _max:
                _max = k
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return _max
                
        
        