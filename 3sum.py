#my time limit exceed solution
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        judge = []
        for i in range(len(nums)):
            for j in range(i):
                for k in range(j):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[k], nums[j], nums[i]]
                        temp2 = set(temp)
                        if temp2 not in judge:
                            triplets.append(temp)
                            judge.append(temp2)
        return triplets

#my improved but still time limit exceep solution:
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        for k in range(2,len(nums)):
            for j in range(1,k):
                twosum = nums[k]+nums[j]
                try:
                    id = nums[:j].index(-twosum)
                    temp = sorted([nums[k],nums[j],nums[id]])
                    if temp not in triplets:
                        triplets.append(temp)
                except:
                    continue
        return triplets

#optimized solution in discussion:
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: #i>0 here important to avoid nums[-1] == nums[0] = 0
            continue
        l, r = i+1, len(nums)-1
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
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

#some sampled fast solution:
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret, pos, neg, counts = [], [], [], {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
                if n >= 0:
                    pos.append(n)
                elif n < 0:
                    neg.append(n)

        if 0 in counts and counts[0] > 2:
            ret.append([0, 0, 0])

        pos.sort()
        neg.sort()

        for p in pos:
            for n in neg:
                tmp = - p - n
                if tmp in counts:
                    if tmp < n or tmp > p:
                        ret.append([n, p, tmp])
                    elif (tmp == p or tmp == n) and counts[tmp] > 1:
                        ret.append([n, p, tmp])

        return ret
