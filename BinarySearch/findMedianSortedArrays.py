# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x = len(nums1)
        y = len(nums2)
        start = 0
        end = x
        while start<=end:
            partitionX = (start+end)/2
            partitionY = (x+y+1)/2 - partitionX
            if partitionX == 0:
                maxLeftX = float('-inf') 
            else:
                maxLeftX = nums1[partitionX-1]
            if partitionX == x:
                minRightX = float('inf')
            else:
                minRightX = nums1[partitionX]
            if partitionY == 0:
                maxLeftY = float('-inf')
            else:
                maxLeftY = nums2[partitionY - 1]
            if partitionY == y:
                minRightY = float('inf')
            else:
                minRightY = nums2[partitionY]
            
            if (maxLeftX <= minRightY) and (maxLeftY <= minRightX):
                if (x+y)%2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX,minRightY))/2.0
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX>minRightY:
                end = partitionX - 1
            else:
                start = partitionX + 1
            