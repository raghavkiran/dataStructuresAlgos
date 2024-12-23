class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)

        if self.min:
            if x < self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self):
        if self.stack[-1] == self.min[-1]:
            self.min.pop()

        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]


obj = MinStack()
obj.push(4)
obj.push(5)
obj.push(2)
obj.push(8)
obj.push(10)

print("MinStack is ")
print(obj.getMin())

