# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(word):
        n = len(word)
        longest = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if word[j] in seen: break
                seen.add(word[j])
            longest = max(len(seen), longest)
        return longest
 
print(Solution.lengthOfLongestSubstring('abcabcabd'))
