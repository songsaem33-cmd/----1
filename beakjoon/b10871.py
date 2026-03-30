N, X = map(int, input().split())
#print(N, X)
A = input().split()
#print(A)

for i in range(len(A)):
	if int(A[i]) < X:
		print(A[i], end=' ')