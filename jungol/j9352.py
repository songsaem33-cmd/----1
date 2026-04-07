lst = []

for i in range(50):
    x = input()
    lst.append(x)

print(*lst[::-1])