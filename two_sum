class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        unseen = nums
        for i,num in enumerate(nums):
            temp = target - num
            if temp in seen.keys():
                return seen[temp],i
            else:
                seen[num] = i
            