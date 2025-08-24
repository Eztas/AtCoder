N, Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

total = 0
for n in range(N):
    total += min(A[n], B[n])

for q in range(Q):
    query = list(input().split())
    c = query[0]
    X = int(query[1])
    V = int(query[2])

    total -= min(A[X - 1], B[X - 1])

    a = A[X - 1]
    b = B[X - 1]

    if c == 'A':
        A[X - 1] = V
    else:
        B[X - 1] = V

    total += min(A[X - 1], B[X - 1])

    print(total)
