S = input()

S_sorted = sorted(S)

if S_sorted[0] == S_sorted[1]:
    print(S_sorted[-1])
else:
    print(S_sorted[0])
    