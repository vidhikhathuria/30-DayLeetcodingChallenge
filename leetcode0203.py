# Problem Link : https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.minVal = []
        self.stack = []
        

    def push(self, x: int) -> None:
        if not len(self.minVal) or self.minVal[-1] >= x:
            self.minVal.append(x)
        self.stack.append(x)
        

    def pop(self) -> None:
        if self.stack[-1] == self.minVal[-1]:
            self.minVal.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()