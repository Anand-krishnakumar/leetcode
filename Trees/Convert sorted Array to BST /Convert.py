class Solution(object):     
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 0:
            k = len(nums)//2
            root = TreeNode(nums[k])
            root.left = self.sortedArrayToBST(nums[:k])
            root.right = self.sortedArrayToBST(nums[k+1:])
            return root
        else:
            return None