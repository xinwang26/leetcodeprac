# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#my initial solution:
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right)) +1
#more concise solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right))) if root else 0

#non-recursive solution: recursive sometimes is slower (here not), this approach visit all nodes by level
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        counter = 0
        
        level = [root] if root else []
        while level:
            counter += 1
            queue = []
            for i in level:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            level = queue
        return counter
