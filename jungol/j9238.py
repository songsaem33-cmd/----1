N = int(input())
M = int(input())

print(N if N > M else M)


A, B, C = map(int,input().split())

print(A if A <= B and A <= C else B if B <= A and B <= C else C)