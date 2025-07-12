A = int(input())
N = int(input())

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

total = 0
for n in range(N):
    n_str = str(n)
    n_a = base10int(n, A)
    if n_str == n_str[::-1] and n_a == n_a[::-1]:
        total += n

print(total)
