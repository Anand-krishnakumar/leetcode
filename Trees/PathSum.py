# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def check(root, curr_sum, sum):
            if root is None:
                return False
        
            if curr_sum+root.val == sum:
                if not root.left and not root.right:
                    return True
            curr_sum += root.val 
            if root.left and root.right:
                return check(root.left,curr_sum, sum) or check(root.right, curr_sum, sum)
            elif root.left:
                return check(root.left,curr_sum, sum)
            elif root.right:
                return check(root.right, curr_sum, sum)
            else:
                return False
        return check(root, 0, sum)
        