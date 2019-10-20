# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    # Attempt 1 - Brute Force, converting to a string and slicing
    def reverse_1(x):
        if x<0:
            x = -1*x
            xr = -1*int(str(x)[::-1])
        else:
            xr = int(str(x)[::-1])
        return xr
    
print(Solution.reverse_1(123456789))
