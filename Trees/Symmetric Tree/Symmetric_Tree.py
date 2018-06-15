# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(t1, t2):
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            else:
                if t1.val == t2.val:
                    return check(t1.left, t2.right) and check(t1.right, t2.left)
                else:
                    return False
        return check(root, root)