# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        result = []
        def paths(node, left, result):
            if node.left is None and node.right is None:
                result.append(left+str(node.val))
            if node.left:
                paths(node.left, left+str(node.val)+"->",result)
            if node.right:
                paths(node.right, left+str(node.val)+"->", result)
        paths(root, '', result)
        return result