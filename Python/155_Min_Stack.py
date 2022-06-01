class MinStack:

    def __init__(self):
        self.stack = []
        self.M = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        M = self.M
        M.append(val if not M else min(val,M[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.M.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.M[-1]

if __name__ == "__main__":
    
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    print(stack.getMin())
    stack.push(-3)