H, W = map(int,input().split()) # それぞれの変数に数値を渡す
h = H / 100
bmi = W / h / h
if bmi >= 25:
    print("Yes")
else:
    print("No")
