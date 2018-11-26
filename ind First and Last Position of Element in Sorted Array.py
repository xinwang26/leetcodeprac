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
        if target < nums[0] or target > nums[-1]:
            return [-1,-1]
        while left < right:
            for idx in [left,(left+ right)//2,right]:
                if target == nums[idx]:
                    mid = idx
                    break
            if mid>=0:
                break
            elif target < nums[(left + right)//2]:
                right = (left + right)//2+1
            elif target > nums[(left + right)//2]:
                left = (left + right)//2-1
        left1 = mid; right1 =mid
        while left-1 >=0 and nums[left] == nums[mid]:
            left -=1
        while right+1 <= len(nums)-1 and nums[right] == nums[mid]:
            right +=1
        return [left,right]
