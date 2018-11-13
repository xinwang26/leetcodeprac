#math solution 144ms
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # tb = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        v = [1000, 500, 100, 50, 10, 5, 1]
        a = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        strn = ''
        remain = ''
        for i in range(7):
            strn = strn + a[i]*(num // v[i])
            num %= v[i]
            # print(num,v[i],strn)
            k = 10 ** (len(str(num)) -1)
            # print(k)
            if -(num//k)*k % v[i] == k:
                remain = a[v.index(k)]+ a[i]
                strn = strn + remain
                num  -= (v[i]-k)
                # print(num,v[i],k,strn)
                # print(num)
        return strn

#faster solution 124ms, do not be trapped by numbers this is just a projection problem but not that even:
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # tb = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        v = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        a = ['M','CM','D','CD','C','XC','L','XL', 'X','IX', 'V','IV', 'I']
        strn = ''
        for i in range(len(v)):
            strn = strn + a[i]*(num // v[i])
            num %= v[i]
        return strn