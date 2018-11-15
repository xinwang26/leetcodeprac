# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        order = {}
        l = head
        i = 1
        while l.next:
            order[i] = l
            i+=1
            l = l.next
        order[i] = l
        if max(order.keys()) ==1:
            return None
        idx = max(order.keys()) +1 - n
        # print(idx, max(order.keys()) ,n)
        if idx == max(order.keys()):
            order[idx-1].next = None
        elif idx == 1:
            head = order[2]
        else:
            order[idx-1].next = order[idx+1]    
        return head
