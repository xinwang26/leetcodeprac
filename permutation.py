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