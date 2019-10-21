# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Coud you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(num):
        if num<0:
            return False
        else:
            if str(num)[::-1] == str(num):
                return True
            else:
                return False
	
num = 22122
print(Solution.isPalindrome(num))