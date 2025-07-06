N = int(input())
S = []

for n in range(N):
    s = input()
    S.append(s)

combinations = set()

for i in range(N):
    for j in range(N):
        if i != j:
            combinations.add(S[i] + S[j])
            
print(len(combinations))
