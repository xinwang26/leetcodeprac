
#the sampled faster solution is not really faster
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) ==0 or (len(nums)==1 and nums[0]!=target):
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        left = 0
        right = len(nums)-1
        while left < right:
            # print(left,right,(left + right)//2)
            for idx in [left,(left + right)//2,right]:
                if nums[idx] == target:
                    return idx
            if target > nums[left]:
                if target < nums[(left + right)//2] or nums[(left + right)//2]< nums[left]:
                    # print('case0')
                    right = (left + right)//2 -1
                else:
                    # print('case1')
                    left = (left + right)//2 +1
            elif target < nums[right]:
                if (target > nums[(left + right)//2]) or (nums[(left + right)//2]> nums[right]):
                    # print('case2')
                    left = (left + right)//2 +1
                    # print(left,right)
                else:
                    # print('case3')
                    right = (left + right)//2 -1
            else:
                return -1
        return -1   
                