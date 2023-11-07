class MinStack(object):

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val):
        self.st.append(val)
        val = min(val, self.minst[-1] if self.minst else val)
        self.minst.append(val)
    
    def pop(self):
        self.st.pop()
        self.minst.pop()


    def top(self):
        return self.st[-1]

    def getMin(self):
        return self.minst[-1]


# Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()