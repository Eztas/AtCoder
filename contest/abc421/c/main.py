N = int(input())
S = input()

# 実際に移動させる必要はない

# 解説
# 計算量的に一度にABABのパターンとBABAのパターン両方を調べる余裕がある
# そのうち最小を持ってくればいい
# この場合、A持ってきて、次はBとかをやらなくても、
# Aだけを持ってくるパターンさえ計算すれば解決
# 2*5*10^5 *2=2*10^6しかないから成り立つ
# AB, BAのパターンのAの正解のインデックスと実際のインデックスの差分合計を計算

countab = 0
countba = 0

indexA = []
# 今のBの位置のリスト
# これらを全部1, 3, 5の変化できればいい
for n in range(2*N):
    if S[n] == 'A':
        indexA.append(n)

idx = 0
for n in range(0, 2*N, 2):
    countab += abs(indexA[idx] - n)
    idx += 1

idx = 0
for n in range(1, 2*N, 2):
    countba += abs(indexA[idx] - n)
    idx += 1

print(min(countab, countba))
