H, W = map(int,input().split()) # それぞれの変数に数値を渡す

bmi = W / H / H * 100 * 100
if bmi >= 25:
    print("Yes")
else:
    print("No")
