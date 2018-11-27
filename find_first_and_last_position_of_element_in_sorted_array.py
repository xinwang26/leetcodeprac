class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) -1
        mid = -1
        if len(nums) <1 or target < nums[0] or target > nums[-1] or (len(nums) == 1 and nums[0]!=target):
            return [-1,-1]
        if len(nums) ==1 and nums[0]==target:
            return [0,0]
        while left < right:
            for idx in [left,(left+ right)//2,right]:
                if target == nums[idx]:
                    mid = idx
                    break
            if mid>=0:
                break
            elif target < nums[(left + right)//2]:
                right = (left + right)//2-1
            elif target > nums[(left + right)//2]:
                left = (left + right)//2+1
        if mid<0:
            return [-1,-1]
        left = mid; right =mid
        while left-1 >=0 and nums[left-1] == nums[mid]:
            left -=1
        while right+1 <= len(nums)-1 and nums[right+1] == nums[mid]:
            right +=1
        return [left,right]