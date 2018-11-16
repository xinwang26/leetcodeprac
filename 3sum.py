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
    for i in range(len(nums)-2):
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
                while l < r and nums[r] == nums[r-1]: #note that l<r must come first otherwise first confirm nums[r-1] / [m+1] could out of index
                    r -= 1
                l += 1; r -= 1
    return res
#slighly improved if exclude bad case first
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
                    if tmp < n or tmp > p: #this restriction avoid any duplicated triplet
                        ret.append([n, p, tmp])
                    elif (tmp == p or tmp == n) and counts[tmp] > 1: #this won't generate duplicate since pos and neg do not have any duplicate
                        ret.append([n, p, tmp])

        return ret

#tried to remember but twisted result, 500ms slower than last
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        result, pos, neg, counts = [],[],[],{}
        #seprate the positive and negative
        for n in nums:
            if n in counts.keys():
                counts[n] +=1
            else:
                counts[n] = 1
            if n>0 and n not in pos:
                pos.append(n)
            elif n<0 and n not in neg:
                neg.append(n)
        try:
            if counts[0] >2:
                result.append([0,0,0])
        except:
            0
        #sort the numbers then start calc
        pos.sort();neg.sort()
        for p in pos:
            for n in neg:
                s = -(p+n)
                if s < p and s > n and s in counts.keys():
                    result.append([n,s,p])
                elif s == n or s==p:
                    if counts[s] >1:
                        result.append([n,s,p])
        return result

#7/16 morning solution
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #solution1
        if len(nums)<3:
            return []
        nums.sort()
        result = []
        for l in range(len(nums)-2):
            if l >0 and nums[l-1] == nums[l]:
                continue
            m, r = l+1, len(nums) - 1
            if nums[l] + nums[m] + nums[m+1] > 0:
                break
            if nums[l] + nums[r] + nums[r-1] < 0:
                continue
            while m<r:
                s = nums[l] + nums[m] + nums[r]
                if s <0:
                    m += 1
                elif s >0:
                    r -= 1
                else:   
                    result.append([nums[l],nums[m],nums[r]])
                    while m <r and nums[m] == nums[m+1]:
                        m+=1
                    while m <r and nums[r] == nums[r-1]:
                        r-=1
                    m +=1
                    r -=1
        return result


#11/16 review:
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #solution1
        pos, neg, result, counts = [],[],[],{}
        for n in nums:
            if n in counts.keys():
                counts[n]+=1
            else:
                counts[n] =1
                if n >=0:
                    pos.append(n)
                elif n<0:
                    neg.append(n)
                    
        if 0 in counts.keys() and counts[0] >2:
            result.append([0,0,0])
        
        pos.sort();neg.sort()
        for p in pos:
            for n in neg:
                remain = -(p+n)
                if remain in counts.keys():
                    if remain > p or remain < n:
                        result.append([n,p,remain])
                    elif (remain == p or remain ==n) and counts[remain] >1:
                        result.append([n,p,remain])
#this one slower than earlier one because used "keys()", when check in dictionary, could use the dictionary itself                        
        return result

