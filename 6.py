class Queue:
    def __init__(self):
        self.items = []
    def Append(self,a):
        self.items.append(a)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def Uzunlik(self):
        return len(self.items)

qoq = Queue()
qoq.Append(2)
qoq.Append(5)
qoq.Append(9)
qoq.Append(23)
qoq.Append(12)
qoq.Append(45)
qoq.Append(3)
qoq.Append(23)
qoq.Append(35)
qoq.Append(86)
qoq.Append(33)
print(qoq.items)
print(qoq.pop())
print(qoq.items)
print(qoq.peek())
print(qoq.Uzunlik())