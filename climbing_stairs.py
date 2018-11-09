class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        import operator as op
        from functools import reduce
        def ncr(n, r):
            r = min(r, n-r)
            numer = reduce(op.mul, range(n, n-r, -1), 1)
            denom = reduce(op.mul, range(1, r+1), 1)
            return numer//denom
        combination = 1
        for i in range(1,n//2+1):
            combination += ncr(n-i,i)
        return combination

#normal recursive solution: -- this one is so simple
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
