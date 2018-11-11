class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <=1:
            return s
        delim = '#' if '#' not in s else '|'
        T = delim + delim.join([c for c in s]) + delim
        print(T)
        maxl = 1
        maxt = T[:3]
        cent,maxr = 1,1
        i = 2
        Rs = [1,2]
        j = 1
        while i < len(T):
            r = min(max(maxr - i,1), Rs[2*cent -i]) #radius of i  
            while r <= min(i,len(T)-i-1):
                if T[i-r] != T[i+r]:
                    break
                r+=1
            Rs.append(r)
            # print(T)
            print(i,r,maxl,T[i-(r-1):i+r])
            maxt = T[i-(r-1):i+r] if r -1 >=maxl else maxt
            maxl = r -1 if r -1 >maxl else maxl
            print(maxt)
            maxr = i+r if i+r >maxr else maxr
            cent = i if i+r >maxr else cent
            i+=1
        print(T,len(T))
        print(Rs,len(Rs))
        return maxt.replace(delim,'')