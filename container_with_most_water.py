class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        maxvol = 0
        while l < r:
            if height[l] <= height[r]:
                maxvol = max(maxvol,height[l]*(r-l))
                l+=1
            else:
                maxvol = max(maxvol,height[r]*(r-l))
                r-=1
        return maxvol