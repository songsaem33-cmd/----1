N = int(input())
M = int(input())

if N >= 3 and M >= 3:
    print("High")
elif N >= 3 or M >= 3:
    print("Mid")
else:
    print("Low")