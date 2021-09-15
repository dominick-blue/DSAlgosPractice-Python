class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push('Hello World')
    print(s.pop())
    print(s)
    print(s.peak())
    print(s.size())
