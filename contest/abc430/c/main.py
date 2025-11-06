N, A, B = map(int,input().split())
S = input()

count = 0
a_count = 0
b_count = 0
ab_counts = []

def count_a(l, r):
    if l > r: return 0
    return ab_counts[r][0] - ab_counts[l][0]

def count_b(l, r):
    if l > r: return 0
    return ab_counts[r][1] - ab_counts[l][1]

if len(set(S)) == 1:
    if S[0] == 'b':
        print(0)
        exit()

for n in range(N):
    if S[n] == 'a':
        a_count += 1
    else:
        b_count += 1
    ab_counts.append([a_count, b_count])

# 尺取法での計算
# 「2つのポインター（lとr）を使い、区間をスライドさせながら探索する」こと
# 区間[l, r]の長さや、区間内の値が、lやrの移動に対して単調に変化するという性質（単調性）を持つ問題
r_a = 0  # 'a'の条件 (>= A) を満たす最小の終点 r
r_b = 0  # 'b'の条件 (< B) を満たさなくなる最小の終点 r (exclusive)
for l in range(N):
    # 'a' の条件を満たす最小の r_a を見つける
    while r_a < N:
        a_c = count_a(l, r_a)
        if a_c >= A:
            break
        r_a += 1
    
    if r_a == N:
        break # r_a が N に達したら、以降の l では条件を満たさない

    # 'b' の条件を満たさなくなる最小の r_b を見つける (r_b は r_a 以上で開始)
    r_b = max(r_b, r_a) # r_b は l の増加に対して単調増加
    while r_b < N:
        b_c = count_b(l, r_b)
        if b_c >= B: # B 個未満の条件を満たさない（>= B になった）
            break
        r_b += 1

    # 条件を満たす r の範囲は [r_a, r_b - 1]
    # r の個数は (r_b - 1) - r_a + 1 = r_b - r_a
    count += (r_b - r_a)

print(count)

