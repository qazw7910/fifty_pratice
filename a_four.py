class Stack1():
    def __init__(self):
        self.data = []

    def push(self, x):
        return self.data.append(x)

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        return self.data[-1]

    def max_num(self):
        return max(self.data)

    def min_num(self):
        return min(self.data)

class Stack2(list):
    def push(self, x):
        return self.append(x)

    def top(self):
        return self[-1]

    def max_num(self):
        return max(self)

    def min_num(self):
        return min(self)

if __name__ == '__main__':

    stack = Stack1()
    stack.push(3)
    stack.push(2)
    stack.push(8)
    stack.push(6)
    stack.push(5)
    print(stack.pop())
    print(stack.top())
    print(stack.max_num())
    print(stack.min_num())