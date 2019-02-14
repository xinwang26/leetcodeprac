#dictionary method my own, permute 7 takes 88ms
#dictionary method my own 
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <=1:
            return [nums]
        nums = sorted(nums)
        global result
        result = [nums[:]]
        def appendnextpermute(currpermut):
            global result
            # print('bf',currpermut,result)
            for i in reversed(range(len(nums))):
                if i-1>=0 and currpermut[i-1] < currpermut[i]:
                    for j in reversed(range(len(nums))):
                        if currpermut[j] > currpermut[i-1]:
                            currpermut[i-1],currpermut[j] = currpermut[j],currpermut[i-1]
                            currpermut[i:] = sorted(currpermut[i:])
                            # result = result +[currpermut]
                            result.append(appendnextpermute(currpermut[:]))
                            return currpermut
        appendnextpermute(nums)
        result =  list(filter(None,result) ) + [nums] 
        # result = result.remove(null) + [nums]
        return result


#my non dictionary method, permute 7 otake 76ms
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        results = []
        global results
        # global results
        def recur_permute(nums,begin):
            global results
            if begin == len(nums):
                results.append(nums)
                return
            else:
                recur_permute(nums[:],begin+1)
                for i in range(begin+1,len(nums)):
                    nums[begin],nums[i] = nums[i],nums[begin]
                    recur_permute(nums[:],begin+1)
                    nums[begin],nums[i] = nums[i],nums[begin]
        recur_permute(nums,0)
        return results

#sampled 44ms solution, not really faster but different idea from mine, 76ms for permute 7 
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [[nums[0]]]
        prev_permutations = self.permute(nums[1:])
        permutations = []
        for i in range(len(prev_permutations)):
            for j in range(len(prev_permutations[i])+1):
                permutation = prev_permutations[i][:j] + [nums[0]] + prev_permutations[i][j:]
                permutations.append(permutation)
        
        return permutations
        