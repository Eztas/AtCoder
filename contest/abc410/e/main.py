N, H, M = map(int,input().split())
# 実際はforループで順番に倒すとかではなく
# 総合計を計算して出力するはず
# 体力を1,3番目に, 魔法を2, 4, 5番目に使うと最も敵を倒せる、みたいに
for n in range(N):
    A, B = map(int,input().split())
    
    if A <= H and A < B:
        H = H - A
    elif B <= W and A >= B:
        W = W - B
