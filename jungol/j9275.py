lst = []

while True:
    N = int(input())

    if N == 0:
        break

    lst.append(N)

for i in range(len(lst)):
    print(f"N = {lst[i]}")