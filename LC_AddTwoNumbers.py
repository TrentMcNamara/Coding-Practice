# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
    def addTwoNumbers(list1, list2):
        l1 = ''
        l2 = ''
        l3 = []
        for i in list1: l1 += str(i)
        for i in list2: l2 += str(i)
        ans = str(int(l1[::-1]) + int(l2[::-1]))
        for i in ans: l3.append(i)
        
        return l3
    

list1 = [1,2,3]
list2 = [4,5,6]
print(Solution.addTwoNumbers(list1, list2))
