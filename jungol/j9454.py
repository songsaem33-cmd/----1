N, M = map(int,input().split())
def i(a, b):
    return a + b
    
def l(a, b):
    return abs(a - b)

print("두 수의 합 =",i(N, M))
print("두 수의 차 =",l(N, M))