class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x <0 else 1
        x = sign *x
        y = 0
        while x >0:
            y = y*10 + x%10
            x = x //10
            if (y*sign >= 2**31-1) or (y*sign <= -2**31):
                return 0
        y *= sign 
        return y