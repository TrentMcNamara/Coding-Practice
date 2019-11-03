# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

class Solution:
    def maxArea(vector):
        area = 0
        for i in range(0,len(vector)):
            for j in range(i+1,len(vector)):
                length = j-i
                height = min(vector[i],vector[j])
                if length*height>= area:
                    area = length*height
                    index = [i,j]
              
        return index, area

vector = [1,8,6,2,5,4,8,3,7]    
print(Solution.maxArea(vector))