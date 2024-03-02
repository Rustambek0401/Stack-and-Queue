class Stack:
    def __init__(self):
        self.data = []
    def push(self,son):
        self.data.insert(0,son)
    def pop(self):
        # sun =  self.data
        # if not sun:
        #     self.data.pop()
        # else:
        #     print("XATO")
        self.data.pop()
    def pek(self):
        if not self.data():
            return self.data[-1]
        else:
            print("XATO")
    def uzunlik(self):
        return len(self.data)
sus = Stack()
sus.push(2)
sus.push(4)
sus.push(8)
sus.push(12)
sus.push(5)
print(sus.data)
sus.pop()
print(sus.data)

