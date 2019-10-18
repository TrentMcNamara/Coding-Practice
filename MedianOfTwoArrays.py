# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

class Solution:
    def findMedianSortedArrays(list1, list2):
        list = sorted(list1+list2)
        if len(list) % 2 == 0: #---even numbers
            median = (list[int(len(list)/2 - 1)] + list[int(len(list)/2)])/2
        else: #---odd numbers
            median = list[int(len(list)/2 - 0.5)]
        
        return int(median)
        
list1 = [-100,1,2,2,2,2]
list2 = [3,4,5,10,500,1000,1000,1000]
print(Solution.findMedianSortedArrays(list1, list2))