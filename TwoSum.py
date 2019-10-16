# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    #---Attempt 1: Brute Force Solution 
    def twoSum_brute(nums, target):
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
    
    #---Attempt 2
    def twoSum_two(nums, target):
        solved = 0
        for i in nums:
            if target - i in nums and (i != target-i):
                return [nums.index(i), nums.index(target-i)]
                solved = 1
        if (solved != 1):
            return 'no solution'

list = [1,2,3,6,10]
target = 9    
print(Solution.twoSum_brute(list, target))
print(Solution.twoSum_two(list, target))