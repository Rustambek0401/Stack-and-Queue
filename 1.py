class Stack:
    def __init__(self):
        self.data = []
    def bosh(self):
        # boshligini aniqlaydi
        #agar bosh bo'lsa True afar bosh bo'lmasa Foal qaytadi
        return len(self.data) == 0
    def Pop(self):
        # boshligini tekshiradi
        #agar bosh bo'lmasa ifni ichiga kiradi
        if not self.data1():
            return self.data.pop()
        else:
            print("????? XATOLIK ??????")
    def Push(self,data):
        self.data.insert(0,data)
    def Peek(self):
        if not self.data():
            return self.data[-1]
        else:
            print("??? XATO ???")
    def Uzunlik(self):
        return len(self.data)
sus = Stack()
# print(" 0 kiritsangiz son kiritish to'xtaydi va natijani ekrakga chiqaradi ")
# while True:
#     s = int(input("Son: "))
#     if s == 0:
#         sus.Push(s)
#         print(sus.data)
#         break
sus.Push(2)
sus.Push(4)
sus.Push(8)
sus.Push(12)
sus.Push(5)
print(sus.data)



