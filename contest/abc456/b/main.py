A1 = list(map(int,input().split())) # 配列で返す
A2 = list(map(int,input().split())) # 配列で返す
A3 = list(map(int,input().split())) # 配列で返す

# 4, 5, 6

count456 = 0

count456 += A1.count(4)*A2.count(5)*A3.count(6)
count456 += A1.count(4)*A2.count(6)*A3.count(5)
count456 += A1.count(5)*A2.count(4)*A3.count(6)
count456 += A1.count(5)*A2.count(6)*A3.count(4)
count456 += A1.count(6)*A2.count(5)*A3.count(4)
count456 += A1.count(6)*A2.count(4)*A3.count(5)

print(count456/256)
