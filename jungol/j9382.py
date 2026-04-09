A = "apple orange banana"
B = "   Hello world!   "

retA = A.split()

idx = len(retA)

for x in range(idx-1, -1, -1):
    print(retA[x], end=' ')
print()
print(B)
print(B.strip())