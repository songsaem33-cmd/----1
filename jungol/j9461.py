a, b = map(int,input().split())

def calc():
    global a, b
    if a > b:
        a //= 2
        b *= 2
    else:
        b //= 2
        a *= 2

calc()
print(a, b)