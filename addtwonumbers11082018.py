# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        last = start =l= ListNode(0)
        carryover = 0
        while l1 or l2:
            # print(start.val)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            digit = v1 + v2 + carryover
            carryover = 1 if digit >9 else 0
            digit = digit - 10 if digit >9 else digit
            start.next = ListNode(digit)
            last = start
            start = start.next if start else None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carryover ==1:
            last.next.next = ListNode(1)
        return l.next
 
 #Runtime: 108 ms, faster than 95.20% of Python3 online submissions for Add Two Numbers.
            
