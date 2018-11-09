
'''time limit exceed because recursive is always slow, and since this is simple summation, 
there is no need to do recursion, iteration/loop is very enough'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        else:
            return max(self.rob(nums[:-2]) + nums[-1], self.rob(nums[:-1]))

#very concise solution:
# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max( f(k-2) + nums[k], f(k-1) )
class Solution:
    def rob(self, nums):
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now
#my remember and practice:      
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: #adding these two lines improves speed
            return 0
        currmax = 0
        lastmax =0
        for i in range(len(nums)):
            lastmax, currmax = currmax, max(currmax, lastmax + nums[i]) 
        return currmax