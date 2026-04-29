class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_min = float('inf')

    def push(self, val: int) -> None:
        self.cur_min = min(self.cur_min, val)
        self.stack.append([val, self.cur_min])
        
    def pop(self) -> None:
        self.stack.pop()

        if self.stack:
            self.cur_min = self.stack[-1][1]
        else:
            self.cur_min = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
