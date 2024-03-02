class Queue:
    def __init__(self):
        self.items = []
    def Append(self,a):
        self.items.append(a)
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print(" XATALOK BORR")
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("XATOLIK BOR !?!?!?!?!?!")
    def Uzunlik(self):
        return len(self.items)

qoq = Queue()
# qoq.Append(2)
# qoq.Append(5)
# qoq.Append(9)
# qoq.Append(23)
# qoq.Append(12)
# print(qoq.items)
while True:
    a = int(input("A:  "))
    qoq.Append(a)
    if a == 0:
        break
print(qoq.items)