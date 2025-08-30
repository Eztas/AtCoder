X, Y = map(int,input().split()) # a_1, a_2

a = [0] * 10
a[0] = X
a[1] = Y

# 10->01などにもうまく対応
def reverse_int(x):
    return int(str(x)[::-1])

for i in range(2, 10):
    a[i] = reverse_int(a[i-1] + a[i-2])

print(a[9])
