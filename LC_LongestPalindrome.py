# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindrome(s):
        res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)] 
        count = 0
        for i in res:
            if i==i[::-1]:
                if len(i)>count:
                    count = len(i)
        return count
        
string = 'Hello'
print(Solution.longestPalindrome(string))
