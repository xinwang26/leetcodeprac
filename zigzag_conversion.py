#my very slow but work solution
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows ==1:
            return s
        numCols = len(s)//numRows if len(s)%numRows ==0 else len(s)//numRows+1  
        numCols += (numCols -1)* (numRows -2)
        t = [' ']*(numCols*numRows)
        print(len(t),numRows,numCols)
        rchg = 1
        rindex = []
        cindex = []
        r = 0
        c = 0
        for count in range(len(s)):
            # if count >100:
                # print(count,r,c)
            t[r*numCols+c] = s[count]
            rindex.append(r)
            cindex.append(c)
            r += rchg
            if rchg == -1:
                c+=1
            if r in (numRows -1,0):
                rchg *= -1
        #     print(t)
        # print(rindex)
        # print(cindex)
        # print(t)
        return ''.join(t).replace(' ','')


# a fast and clean method by just append letters by rows:
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows ==1:
            return s
        rows = [''] * numRows
        rchg = 1
        r = 0
        for count in range(len(s)):
            rows[r] =  rows[r] + s[count]
            r += rchg
            if r in (numRows -1,0):
                rchg *= -1
        return ''.join(rows)