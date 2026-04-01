A, B, C = map(int,input().split())

if A > B and A > C:
    print(f"MAX: {A}")
elif B > A and B > C:
    print(f"MAX: {B}")
else:
    print(f"MAX: {C}")