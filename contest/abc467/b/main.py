N = int(input())
A = []
B = []
S = []

for n in range(N):
    a, b, s = input().split()

    A.append(int(a))
    B.append(int(b))
    S.append(s)

loss = 0
for i in range(N):
    if S[i] == "keep":
        loss += B[i] - A[i]

print(loss)
