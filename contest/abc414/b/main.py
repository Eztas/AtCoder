N = int(input())
count = 0
S = ""
isTooLong = False
for n in range(N):
    c, l = map(str, input().split()) # strをつけないとmapできない

    count += int(l)
    if count > 100:
        isTooLong = True
        break

    for i in range(int(l)):
        S += c # appendではなく、+=で文字列を連結する

if isTooLong:
    print("Too Long")

else:
    print(S)
