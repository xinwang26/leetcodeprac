#stupid and wrong solution
# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if len(s)%2 != 0:
#             return False
#         mapping = { '(':[1,0,0], ')':[-1,0,0], '[':[0,1,0],']':[0,-1,0],'{':[0,0,1],'}':[0,0,-1]}
#         close = [0,0,0]
#         last = mapping[s[0]]
#         for i in range(len(s)):
#             curr = mapping[s[i]]
#             close= [sum(x) for x in zip(close,curr)]
#             if min(close) <0:
#                 return False
#             elif min(mapping[s[i]]) <0 and max(mapping[s[i-1]])>0 and min([sum(x) for x in zip(mapping[s[i]],mapping[s[i-1]])])<0:
#                 # print(mapping[s[i]],mapping[s[i-1]])
#                 return False
#         if max(close) >0:
#             return False
#         return True

#worked but slow solution:
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        mapping = {  ')':'(', ']':'[','}':'{'}
        left = []
        check = 0
        for d in s:
            if d in mapping.values():
                left.append(d)
                check +=1
            elif d in mapping.keys():
                check -=1
                if check <0 or left[-1] != mapping[d]:
                    return False
                else:
                    left = left[:-1]
        if len(left) >0:
            return False
        return True
#my optimized version:
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        mapping = {  ')':'(', ']':'[','}':'{'}
        stack = []
        for d in s:
            if d in mapping.keys():
                try:
                    last = stack.pop()
                except:
                    return False
                if last != mapping[d]:
                    return False
            else:
                stack.append(d)
        if len(stack) >0:
            return False
        return True