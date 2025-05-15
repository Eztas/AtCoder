R,X = map(int,input().split())

if X == 1:
    if R >= 1600 and R <= 2999:
        print("Yes")
    else:
        print("No")
elif X == 2:
    if R >= 1200 and R <= 2399:
        print("Yes")
    else:
        print("No")
