N, A, B = map(int,input().split())
S = input()

count = 0
a_count = 0
b_count = 0
ab_counts = []
if len(set(S)) == 1:
    if S[0] == 'b':
        print(0)

for n in range(N):
    if S[n] == 'a':
        a_count += 1
    else:
        b_count += 1
    ab_counts.append([a_count, b_count])
