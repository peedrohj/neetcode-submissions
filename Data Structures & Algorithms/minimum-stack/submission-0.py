class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        min_item = self.stack[-1]

        for item in self.stack:
            if item < min_item:
                min_item = item 

        return min_item
