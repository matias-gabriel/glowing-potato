class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        last_element = self.stack[-1] if len(self.stack) else (val, val)
        min_val = val
        if val > last_element[1]:
            min_val = last_element[1]

        self.stack.append((val, min_val))

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack):
            return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
