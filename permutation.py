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
            print(currpermut)
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