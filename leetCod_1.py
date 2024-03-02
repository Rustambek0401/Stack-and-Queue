data = [1,2,3,4,5,6,7,8,9,10]
print(data)
da = []
s = int(input("Target: "))
for i in data:
    # print(f"{i} ++++ {i+1}"
    a = i + (i+1)
    if s == a:
        print(f"Natija :--> {i-1} <--> {i} <--")
        break
    else:
        print(" XATO ")
