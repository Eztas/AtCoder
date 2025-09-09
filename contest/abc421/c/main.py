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

# if文を使えばより簡略に、しかも配列の中でenumerateは使える
indexA = [i for i, char in enumerate(S) if char == 'A']

# これで0, 1-> 2, 3 -> 4, 5で計算できる
for i in range(N):
    countab += abs(indexA[i] - 2 * i)
    countba += abs(indexA[i] - (2 * i + 1))

print(min(countab, countba))
