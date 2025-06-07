N, S = map(int,input().split())
T = list(map(int,input().split()))

sleep = "Yes"
T.insert(0, 0)  # 最初の叩く時間を0に設定

for n in range(N):
  if T[n+1] - T[n] >= S + 0.5: # 次に叩くまでS+0.5未満で叩けたら老人は寝ない
    sleep = "No"
    break
  
print(sleep)
