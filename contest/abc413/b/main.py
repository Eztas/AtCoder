N = int(input())
S = []

for n in range(N):
    s = input()
    S.append(s)

count = 0
combinedwords = []

for i in range(N):
    for j in range(N):
        existed = False
        if i == j:
            continue
        else:
            for combinedword in combinedwords:
                if S[i] + S[j] == combinedword:
                    existed = True
                    continue
            if not existed:
                combinedwords.append(S[i] + S[j])
                count += 1

print(count)
