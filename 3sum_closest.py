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