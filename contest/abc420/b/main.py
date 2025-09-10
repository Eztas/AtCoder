N, M = map(int,input().split())

S = []
counts = [0] * N
# N人, M回の投票
for n in range(N):
    s = input()
    S.append(list(s))

def print_horizontal_line(dataList, endChar):
    for idx, data in enumerate(dataList):
        if idx < len(dataList) - 1:
            print(data,end=endChar)
        else:
            print(data)

def my_index_multi(l, x):
    return [i + 1 for i, _x in enumerate(l) if _x == x]

for m in range(M):
    x = 0
    y = 0
    for s in S:
        if s[m] == '0':
            x += 1
        else:
            y += 1

    if x == 0 or y == 0:
        for n in range(N):
            counts[n] += 1
    elif x < y:
        for n in range(N):
            if S[n][m] == '0':
                counts[n] += 1
    else:
        for n in range(N):
            if S[n][m] == '1':
                counts[n] += 1

#print_horizontal_line(counts, ' ')

print_horizontal_line(my_index_multi(counts, max(counts)), ' ')
