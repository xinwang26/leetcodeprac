class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #kadane's algorithm
        max_end_here = nums[0]
        max_so_far = nums[0]
        for i in range(1,len(nums)):
            max_end_here = max(max_end_here + nums[i],nums[i])
            max_so_far = max(max_so_far,max_end_here)
        return max_so_far

#seems for python compare is faster than max function                
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]
        max=nums[0]
        for i in range(1,len(nums)):
            sum=sum+nums[i]
            if (sum<nums[i]) : sum = nums[i]
            if (sum>max):
                max=sum
        return max

        