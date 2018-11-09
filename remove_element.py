class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        long = len(nums)
        i = 0
        while i < long:
            value = nums[i]
            if val== value:
                long = long -1
                nums.pop(i)
            else:
                i+=1