X = int(input())
N = int(input())
prod = 0
for i in range(N):
    a, b = map(int,input().split())
    prod += (a * b)
if X == prod:
    print("Yes")
else:
    print("No")