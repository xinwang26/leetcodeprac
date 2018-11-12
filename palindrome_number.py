class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10 ==0 and x>0):
            return False
        elif x <10:
            return True
        right = 0
        while right < x:
            right = x%10 + 10*right
            x //=10
            if right == x or right * 10 + x%10 ==x:
                return True
        return False

#since only need to compare once, should not put the comparison in loop

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10 ==0 and x>0):
            return False
        elif x <10:
            return True
        right = 0
        while right < x:
            right = x%10 + 10*right
            x //=10
        if right == x or right //10 ==x:
            return True
        else:
            return False
    