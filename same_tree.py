# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#intuition solution-- should try incorporate much special case as possible to improve
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        try:
            if p.val != q.val:
                return false
            else:
                try:
                    leftsame = self.isSameTree(p.left,q.left)
                except:
                    if p.left == None and q.left == None:
                        leftsame = True
                    else:
                        return False
                try:
                    rightsame = self.isSameTree(p.right,q.right)
                except:
                    if p.right == None and q.right == None:
                        rightsame = True
                    else:
                        return False
                return leftsame and rightsame
        except:
            if p == None and q == None:
                return True
            else:
                return False

#more concise solution, not really faster finally:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None or q == None:
            return p == q
                
                
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)