class MinStack:

    def __init__(self):
        self.minStack = []
        self.pre = []
    

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if len(self.pre) == 0:
            self.pre.append(val)
        else:
            self.pre.append(min(val,self.pre[-1]))
        
        return None

    def pop(self) -> None:
        self.minStack.pop(-1)
        self.pre.pop(-1)
        return None

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.pre[-1]
        
