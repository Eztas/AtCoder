N, S = map(int,input().split())
t = list(map(int,input().split()))

sleep = "Yes"
T = [0, t]

for n in range(N-1):
  if T[n+1] - T[n] >= S + 0.5: # 次に叩くまでS+0.5未満で叩けたら老人は寝ない
    sleep = "No"
    break
  
print(sleep)
