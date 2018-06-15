class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        q = []
        q.append(root)
        l = []
        temp = []
        while len(q) > 0:
            node = q.pop(0)
            l.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if len(q) == 0:
                result.append(l)
                q = temp
                temp = []
                l = []
        return result    