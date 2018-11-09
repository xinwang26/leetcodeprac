class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        long = len(nums)
        right = long
        left = 1
        while left < right:
            # print(left,right)
            mid = round((left + right)/2)
            if target <= nums[left-1]:
                # print("case1")
                return left -1
            elif target > nums[right-1]:
                # print("case2")
                return right 
            elif target == nums[mid-1] or (target < nums[mid-1] and target > nums[mid-2]) :
                # print("case3")
                return mid-1
            elif target < nums[mid -1]:
                right = mid
            elif target > nums[mid -1]:
                left = mid+1
        if target > nums[right -1]:
            return right 
        elif target <= nums[left -1]:
            return left - 1
            

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = int((left + right)/2)
            if target <= nums[mid]:
                right = mid -1
            else:
                left = mid +1
        return left
