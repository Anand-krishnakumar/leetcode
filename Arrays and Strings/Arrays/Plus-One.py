# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # #python solution-1
        # b = [str(x) for x in digits]
        # k = int(''.join(b))
        # return [int(x) for x in str(k+1)]
        
        carry = (digits[-1]+1)//10
        digits[-1] = (digits[-1]+1)%10
        
        for i in range(len(digits)-2, -1, -1):
            carry, digits[i] = (carry + digits[i])//10,(carry+digits[i])%10
        if carry:
            digits.insert(0,carry)
        return digits


            