class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if len(nums)<3:
            return None
        result = nums[0]+nums[1]+nums[2]
        for l in range(len(nums)-2):
            m, r = l+1, len(nums)-1
            while m < r:
                s = nums[l] + nums[m] + nums[r]
                result = s if abs(s - target) < abs(result -target) else result
                if s == target:
                    return s
                elif s > target:
                    r -=1
                elif s < target:
                    m +=1
        return result

#sampled answer very fast solution
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
  
        
        res = list()
        nums.sort()
        
        for i in range(len(nums)-2):
            j,k = i+1, len(nums)-1
            if nums[i] + nums[k] + nums[k-1] < target:
                res.append(nums[i] + nums[k] + nums[k-1]) #first check extreme case, smart!
            elif nums[i] + nums[j] + nums[j+1] > target:
                res.append(nums[i] + nums[j] + nums[j+1])
            else:
                while j < k:
                    s = nums[i]+nums[j]+nums[k]
                    res.append(s)
                    if s < target:
                        j +=1
                    elif s > target:
                        k -=1
                    else:
                        return target
                    
        res.sort(key = lambda x:abs(x-target))
        return res[0]

#even worse if check extreme case first
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: #i>0 here important to avoid nums[-1] == nums[0] = 0
                continue
            l, r = i+1, len(nums)-1
            if nums[i] + nums[r] + nums[r-1] < 0 or nums[i] + nums[l] + nums[l+1] > 0:
                continue
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]: #l<r here important
                        l += 1
                    while l < r and nums[r] == nums[r-1]: #note that l<r must come first otherwise first confirm nums[r-1] / [m+1] could out of index
                        r -= 1
                    l += 1; r -= 1
        return res