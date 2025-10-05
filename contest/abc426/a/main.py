X, Y = input().split()

if Y == "Ocelot":
    print("Yes")
elif Y == "Serval":
    if X == "Ocelot":
        print("No")
    else:
        print("Yes")
else:
    if X == "Lynx":
        print("Yes")
    else:
        print("No")
