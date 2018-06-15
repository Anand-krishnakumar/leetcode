class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = []
        def inorder(root):
            if root is not None:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        inorder(root)
        for i in range(len(l)-1):
            if l[i] >= l[i+1]:
                return False
        return True
            