S = input()

# 1桁の数字, A+B*その数値
# 1 -> A, B, 2回
# 2 -> A, B, B, 3回
# 3 -> A, B, B, B, 4回

# 10~19, 3 or 13
# 10 -> A, B, A, 3回
# 11 -> A, A, B, 3回
# 12 -> A, B*9, A, B, B, 13回
# 13 -> A, B*8, A, B, B, B, 13回

# 20~29, 
# 20 -> A, B, B, A, 4回
# 21 -> A, B, A, B, 4回
# 22 -> A, A, B, B, 4回
# 23 -> A, B*9, A, B, B, B, 14回

# 2桁=t_1t_2のとき、t_1<=t_2なら, t_1+2, elseならt_1+12

# 100~
# 100 -> A, B, A, A, 4回
# 101 -> A, B, A, B*9, A, B(101<-090<-09<-10から9回B), 14回
# 102 -> A, B, A, B*8, A, B, B, 14回
# 199 -> A, B, B, A, A, B*9, 14回
# 143 -> (143->810->81->70->7->0)
# 143, 341->018->18

# Sの下一桁が

# 最上位桁が0のときの対応ができていない

count = 0

while True:
    S_number = int(S)
    S_len = len(S)
    last_S = int(S[S_len-1])
    count += last_S
    for idx in range(S_len):
        if int(S[idx]) < last_S:
            S_number += (10 ** (S_len - idx - 1)) * (10 - last_S)       
        else:
            S_number -= (10 ** (S_len - idx - 1)) * last_S

    S_number //= 10
    print(S_number)
    S = str(S_number)
    count += 1

    if S_len == 1:
        break

print(count)
