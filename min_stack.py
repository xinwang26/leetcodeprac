class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack  = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        try:
            if x <= self.minstack[-1]:
                self.minstack.append(x)
        except:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        top = self.stack.pop(-1)
        try:
            if top == self.minstack[-1]:
                self.minstack.pop(-1)
        except:
            return None
        return None

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        try:
            return self.minstack[-1]
        except:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#faster solution:
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x-self.min)
            if self.stack[-1] < 0:
                self.min = x
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] <= 0:
            res = self.min
            self.min -= self.stack.pop()
        else:
            res = self.stack.pop()
        return res
            
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack[-1] > 0:
            return self.stack[-1] + self.min
        else:
            return self.min
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()