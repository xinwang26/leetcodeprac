#my intuition: binary search vertically
#optimal answers:

#1. divide and conquer -- recursive
#2. binary -- start from smallest length in the array -- different from intuition
#3. TRIE

#my divide and conquer solution with error:

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            # print(strs)
            return strs[0]
        elif len(strs) == 2:
            short = min(len(strs[0]),len(strs[1]))
            for i in range(short):
                # print(str(short),strs,"  "+strs[0][:i]," "+strs[1][:i])
                if strs[0][i] != strs[1][i]:
                    return strs[0][:i]
            return strs[0][:short]
        if len(strs)>2:
            print(strs[:(len(strs)-1)//2],strs[(len(strs)-1)//2:])
            return self.longestCommonPrefix([self.longestCommonPrefix(strs[:(len(strs)-1)//2])]+[self.longestCommonPrefix(strs[(len(strs)-1)//2:])])

#fast solution: -- it turs out horizontal scan is faster for python 3
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        exist = False
        first = strs[0]
        result = ""
        
        for i in range(0, len(first)):
            exist = True
            try:
                for word in strs[1:]:
                    if word[i] != first[i]:
                        exist = False
                        break
            except:
                return result
            if exist:
                print(first[i])
                result += first[i]
            else:
                break
                
        
        return result

#11/12 write it again, need to review again:
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)<1:
            return ''
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        result = ''
        for i in range(len(first)):
            iiscommon = True
            try:
                for w in strs[1:]:
                    if w[i] != first[i]:
                        iiscommon = False
                        break
                if iiscommon:
                    result = result + first[i]
                else:
                    return result
            except:
                return result
        return result