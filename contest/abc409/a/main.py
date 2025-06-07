N = int(input())
T = input() # 文字列だから、splitいらない
A = input()

text = "No"

for n in range(N):
    if T[n] == A[n] and T[n] == "o":
        text = "Yes"
        break

print(text)
