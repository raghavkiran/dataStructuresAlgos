class MaxStack:

    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, x):
        self.stack.append(x)

        if self.max:
            if x > self.max[-1]:
                self.max.append(x)
        else:
            self.max.append(x)

    def pop(self):
        if self.stack[-1] == self.max[-1]:
            self.max.pop()

        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getmax(self):
        return self.max[-1]


obj = MaxStack()
obj.push(4)
obj.push(15)
obj.push(2)
obj.push(8)
obj.push(10)

print("maxStack is ")
print(obj.getmax())

