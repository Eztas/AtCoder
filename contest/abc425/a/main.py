N = int(input())

count = 0
for n in range(1, N+1):
    count += ((-1) ** n) * (n ** 3)

print(count)
