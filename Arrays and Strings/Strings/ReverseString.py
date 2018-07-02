# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Recursive Solution
        # l = len(s)
        # if l == 0:
        #     return ''
        # if l == 1:
        #     return s
        # else:
        #     return self.reverseString(s[l/2:]) + self.reverseString(s[0:l/2])
        
        
        # Iterative using list
        # r = list(s)
        # i = 0
        # j = len(s) -1
        # while i < j:
        #     r[i], r[j] = r[j], r[i]
        #     i += 1
        #     j -= 1
        # return ''.join(r)
        
        return s[::-1]
            
            
        