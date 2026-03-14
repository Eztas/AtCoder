from bisect import bisect_left, bisect_right

N, L, R = map(int, input().split())
S = input()

# 各文字の出現位置を記録
char_positions = [[] for _ in range(26)]
for idx, char in enumerate(S):
    char_positions[ord(char) - ord('a')].append(idx)

count = 0

# 各文字について処理
for positions in char_positions:
    n = len(positions)
    if n < 2:
        continue
    
    for i in range(n):
        # positions[i] を基準として、距離が [L, R] の範囲にある位置を探す
        target_min = positions[i] + L
        target_max = positions[i] + R
        
        # 二分探索で範囲を特定
        # 思ったよりゴリ押しで行けた
        # Lの範囲とRの範囲を知ることで、それの差分調べれば行けた
        left = bisect_left(positions, target_min, i + 1) # claude推薦
        right = bisect_right(positions, target_max, i + 1)
        
        count += right - left

print(count)
