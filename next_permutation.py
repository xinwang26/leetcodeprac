class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(1,len(nums))):
            if nums[i-1] < nums[i]:
                for j in reversed(range(len(nums))):
                    if nums[j] > nums[i-1]:
                        nums[i-1],nums[j] = nums[j],nums[i-1]
                        nums[i:] = sorted(nums[i:])
                        return None
        nums.sort()
        return None

#the sampled faster solution not really faster