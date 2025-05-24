N, K = map(int,input().split())
A = list(map(int,input().split()))

num = 1

for n in range(N):
  num = num * A[n]
  len_num = len(str(num))
  
  if len_num >= (K+1):
    num = 1
    
print(num)
