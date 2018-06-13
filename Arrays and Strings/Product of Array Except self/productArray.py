class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [None]*len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            l[i] = left
            left = left * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            l[i] = right*l[i]
            right = right*nums[i]
        return l     
        