N, H, M = map(int,input().split())
# 実際はforループで順番に倒すとかではなく
# 総合計を計算して出力するはず
# 体力を1,3番目に, 魔法を2, 4, 5番目に使うと最も敵を倒せる、みたいに

# ユーザ解説 https://atcoder.jp/contests/abc410/editorial/13313を見た感じ
# Nでループとかはしないらしい,Nのループ内で決めると思っていたが、

# dp[h][m]:=( 体力が h 、魔力が m のときに倒せるモンスターの数の最大値 ) とします。
# 残りの体力と魔力で考える、最小の減り方を考える動的計画法を考えていたが、
# こういう考え方らしい

A = []
B = []
for n in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

dp = [[0] * M for _ in range(H)]

for m in range(M):
    for h in range(H):
        max_enemy = dp[h][m]
        dp[h+1][m] = max(dp[h+1][m], max_enemy)
        dp[h][m+1] = max(dp[h][m+1], max_enemy)

        if max_enemy < N:
            if h + A[max_enemy] <= H:
                dp[h + A[max_enemy]][m] = max(dp[h + A[max_enemy]][m], max_enemy + 1)
            if m + B[max_enemy] <= M:
                dp[h][m + B[max_enemy]] = max(dp[h][m + B[max_enemy]], max_enemy + 1)
