N, A = input().split()
A = int(A)

if N == "M" and A >= 19:
    print("MAN")
elif N == "F" and A >= 19:
    print("WOMAN")
elif N == "M" and A < 19:
    print("BOY")
else:
    print("GIRL")