# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

class Solution:
    def myAtoi(str):
        nums = '0123456789'
        s = ''
        neg = 1
        
        list = []
        for i in str:
            if i in nums :
                list += i  

        for i in list: 
            s += i 
        s = int(s)
        
        iter = 0
        for i in str:
            if i == '-':
                if str[iter+1] in list[0]:
                    neg = -1
            
            iter += 1
        
        return neg*s
        
string = 'hello -4321'
print(Solution.myAtoi(string))