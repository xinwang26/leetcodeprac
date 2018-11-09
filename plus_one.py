class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            for i in reversed(range(len(digits))):
                if digits[i] == 9:
                    digits[i] = 0
                    if i == 0:
                        digits = [1]+digits
                        return digits
                else:
                    digits[i] += 1
                    return digits

#faster solution:
