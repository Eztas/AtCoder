S = input()
S_len = len(S)
count = S_len # Aの回数は必ずS_len回

B_num = 0
for idx in range(S_len):
    B_num += int(S[S_len - idx - 1])
    count += B_num % 10

print(count)
