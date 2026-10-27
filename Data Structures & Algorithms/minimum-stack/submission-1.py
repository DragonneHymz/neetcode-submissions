class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
        else:
            self.minStack.append(val)
        self.stack.append(val)

        

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minStack: return self.minStack[-1]

