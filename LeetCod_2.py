a = int(input("N: "))
d = a
t = 0
while a > 0:
    s = a % 10
    t = t * 10 + s
    a = a // 10
# print(t)
# print(d,"A")
if d == t:
    print("true")
else:
    print("float")