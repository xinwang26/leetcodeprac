#a simple and fast python solution

class Solution(object):
    '''
    To solve the TLE problem, I set two pivots in the partition function, pivotPrev and pivotPost. We just pick the first element as pivot. And if we encounter a node with the same value as pivotPrev, we move the pivotPost one step forward. When partition function returns, the pivotPrev becomes the end node for the former half while the pivotPost becomes the start node for the latter half. In this way, we don't have to sort nodes between two pivots in the next round.

For example, input like 2-3-2-1-4-6-2-5 will become 1-2-2-2-5-6-4-3, and the partition function returns the first node with value 2 and the last node with value 2, then we only have to sort 1 and 5-6-4-3 respectively.
'''
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev
            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]
        
        def quicksort(start, end):
            if start.next != end:
                prev, post = partition(start, end)
                quicksort(start, prev)
                quicksort(post, end)

        newHead = ListNode(0)
        newHead.next = head
        quicksort(newHead, None)
        return newHead.next

#a very short python merge sort solution:
class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next  #fast run two steps, slow is mid pointer, run only one step, pre record the last node of mid pointer, so that the cut could be done
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow))) #recursion is done here, the recursion keep cutting the linked list until all are 1 nodes, I think this is slower than merge starting from two nodes linked

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#my remembered and written solution
class Solution(object):
    def merge(self,h1,h2):
        head = pre = ListNode(-999)
        while h1 and h2:
            if h1.val <= h2.val:
                pre.next, h1 = h1, h1.next
                pre = pre.next
            else:
                pre.next, h2 = h2, h2.next
                pre = pre.next
        pre.next = h1 or h2
        return head.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        midlast , mid ,end = head,head,head
        while end and end.next:
            midlast, mid, end = mid, mid.next, end.next.next
        midlast.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)