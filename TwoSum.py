# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Brute Force Solution 
class Solution:
    def twoSum(nums, target):
        
        solved = 0
        
        index_i = 0
        for i in nums:
            
            index_j = 0
            for j in nums:
                
                if ( i !=j ):
                    summ = i + j
                    
                    if summ == target:
                        return [index_i,index_j]
                        solved = 1
                    
                index_j += 1
            
            index_i +=1
        
        if (solved != 1):
            return 'no solution' 
    
print(Solution.twoSum([1,2,3,6,10], 12))