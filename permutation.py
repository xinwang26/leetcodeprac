#dictionary method my own 
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        global result
        result = [nums]
        def appendnextpermute(currpermut,result):
            # print('bf',currpermut,result)
            for i in reversed(range(len(nums))):
                if i-1>=0 and currpermut[i-1] < currpermut[i]:
                    for j in reversed(range(len(nums))):
                        if currpermut[j] > currpermut[i-1]:
                            currpermut[i-1],currpermut[j] = currpermut[j],currpermut[i-1]
                            currpermut[i:] = sorted(currpermut[i:])
                            # result = result +[currpermut]
                            print('af',currpermut,result)
                            result = result[:] + [appendnextpermute(currpermut[:],result[:])]        
                            return currpermut
        appendnextpermute(nums,[nums])
        return result

#still wrong but better:
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        global result
        result = [nums]
        def appendnextpermute(currpermut):
            # print('bf',currpermut,result)
            global result
            # print(currpermut,result)
            for i in reversed(range(len(nums))):
                if i-1>=0 and currpermut[i-1] < currpermut[i]:
                    for j in reversed(range(len(nums))):
                        if currpermut[j] > currpermut[i-1]:
                            currpermut[i-1],currpermut[j] = currpermut[j],currpermut[i-1]
                            currpermut[i:] = sorted(currpermut[i:])
                            # result = result +[currpermut]
                            print('bf',currpermut,'__',result)
                            temp = appendnextpermute(currpermut[:])
                            if temp != None:
                                result = [currpermut] + temp
                            # print('af',currpermut,result)
                            return result
        appendnextpermute(nums)
        return result

#have dup permute, speed varies a lot from 48ms - 80ms
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