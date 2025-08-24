N, Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for q in range(Q):
    total = 0
    query = list(input().split())
    c = query[0]
    X = int(query[1])
    V = int(query[2])

    if c == 'A':
        A[X - 1] = V
    else:
        B[X - 1] = V

    for n in range(N):
        total += min(A[n], B[n])

    print(total)
