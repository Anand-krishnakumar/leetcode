# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        if len(s) > len(t) or len(s)<len(t):
            return False
        for letter in s:
            if letter in d1.keys():
                d1[letter] += 1
            else:
                d1[letter] = 1
        for letter in t:
            if letter in d2.keys():
                d2[letter] += 1
            else:
                d2[letter] = 1
        for key, value in d1.items():
            if key in d2:
                if value != d2[key]: 
                    return False
            else:
                return False
        return True