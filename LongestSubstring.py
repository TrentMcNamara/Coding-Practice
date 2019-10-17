# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(s):
        count = 0
        for i in set(s):
            if i in s:
                count +=1
        
        return set(s)

 
print(Solution.lengthOfLongestSubstring('abcabcabd'))