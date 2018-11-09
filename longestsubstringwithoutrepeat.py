class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        maxl = 1
        count = 1
        temp = s[0]
        i = 1
        while i <len(s):
            # print(temp)
            if s[i] not in temp:
                # print(s[i])
                count +=1
                # print(count)
                temp  = temp + s[i]
            else:
                temp =  temp[temp.index(s[i])+1:] + s[i]
                count = len(temp)
            maxl = count if count >maxl else maxl
            i+=1
        return maxl