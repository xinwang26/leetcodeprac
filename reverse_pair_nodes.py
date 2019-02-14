# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pos = 0
        newhead = curr = ListNode(0)
        curr.next = head
        while curr.next:
            # print(curr.val)
            if curr.next.next:
                curr.next, curr.next.next, curr.next.next.next = curr.next.next, curr.next, curr.next.next.next
            # print(curr.val,curr.next.val,curr.next.next.val,curr.next.next.next.val)
                curr = curr.next.next
            else:
                break
        return newhead.next