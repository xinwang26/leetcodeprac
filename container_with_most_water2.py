#my initial bad solution:
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <=1:
            return 0
        l, r = 0,len(height)-1
        h = min(height[l],height[r])
        maxa = h*(r-l)
        while l < r:
            if height[l] <= height[r]:
                l+=1
                h = min(height[l],height[r])
                maxa = (r-l)*h if (r-l)*h >maxa else maxa
            else:
                r-=1
                h = min(height[l],height[r]) # redundant and take too much time
                maxa = (r-l)*h if (r-l)*h >maxa else maxa
        return maxa

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <=1:
            return 0
        l, r = 0,len(height)-1
        h = min(height[l],height[r])
        maxa = h*(r-l)
        temp = 0
        while l < r:
            if height[l] <= height[r]:
                temp = (r-l)*height[l]
                l+=1
            else:
                temp = (r-l)*height[r] 
                r-=1
            if temp > maxa:
                maxa = temp
        return maxa