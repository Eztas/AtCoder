S = input()
count = len(S) # Aの回数はSの長さと同じなので、最初から追加

while True:
    last_S = int(S[len(S)-1])
    count += last_S # Bの回数を加算
    next_S = []
    for digit in S:
        if int(digit) < last_S:
            next_S.append(str(10 + int(digit) - last_S))      
        else:
            next_S.append(str(int(digit) - last_S))

    S = next_S[:-1]
    if len(S) == 0:
        break

print(count)
