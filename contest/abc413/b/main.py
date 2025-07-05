N = int(input())
S = []

for n in range(N):
    s = input()
    S.append(s)

count = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            count += 1

print(count)
