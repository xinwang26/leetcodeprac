#my initial slow solution
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        a = ['M','CM','D','CD','C','XC','L','XL', 'X','IX', 'V','IV', 'I']
        mapping = dict(zip(a,v))
        if len(s) == 1:
            return mapping[s]
        i = 0
        n =0
        while len(s)>1:
            if s[:2] in mapping.keys():
                n+=mapping[s[:2]]
                s = s[2:]
            else:
                n+=mapping[s[:1]]
                s = s[1:]
        if s:
            n+=mapping[s]
        return n

#faster by other people, take advantage that small before large means minus:
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = [1000,500,100,50,10,5,1]
        a = ['M','D','C','L', 'X' ,'V', 'I']
        mapping = dict(zip(a,v))
        if len(s) == 1:
            return mapping[s]
        total = 0
        for i in range(len(s) -1):
            if mapping[s[i]] < mapping[s[i+1]]:
                total -= mapping[s[i]]
            else:
                total += mapping[s[i]]
        total += mapping[s[-1]]
        return total