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
        carryover = 0
        last,head = l1,l1
        while l1 and l2:
            l1.val += (l2.val + carryover)
            if l1.val >= 10:
                l1.val -= 10
                carryover = 1
            else:
                carryover = 0
            last,l1,l2 = l1,l1.next,l2.next
        if not (l1 or l2) and carryover ==1:
            last.next = ListNode(0)
        if l2:
            last.next = l2
        last = last.next
        while last:
            last.val += carryover
            if last.val >= 10:
                last.val -= 10
                carryover = 1
                if last.next:
                    last = last.next
                else:
                    last.next = ListNode(1)
                    break
            else:
                break
        return head

## fast and concise solution:
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
        res = ListNode(0)
        cur = res
        base = 0
        while l1 or l2 or base > 0:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + base
            cur.next = ListNode((sum) % 10)
            base = sum // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            cur = cur.next
        return res.next

#my remembered good solution:
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
        carryover = 0
        head= curr = ListNode(0)
        while l1 or l2 or carryover>0:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carryover
            curr.next = ListNode(sum) if sum <10 else ListNode(sum-10)
            carryover = 1 if sum >=10 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return head.next



# 11/08:
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryover = 0 
        start = l1
        while l1 and l2:
            l1.val += (l2.val+carryover)
            carryover = 1 if l1.val>=10 else 0
            l1.val = l1.val if l1.val <10 else l1.val-10
            l1,l2 = l1.next,l2.next
        while l2 or l1 or (carryover >0):
            l1 = l2 if l2 else l1
            l1.val += (l1.val+carryover)
            carryover = 1 if l1.val>=10 else 0
        if carryover>0:
            l1.next = LIstNode(1)
        return start