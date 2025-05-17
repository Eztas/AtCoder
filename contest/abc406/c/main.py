N = int(input())
P = list(map(int,input().split()))

count = 0

for n in range(4, N):
    for i in range(N-n+1):
        flag = True
        # A_1 < A_2である 
        if P[i] >= P[i+1]:
            flag = False
            break

        # A_i−1 ​< A_i > A_i+1 ​を満たす 2 ≤ i <|A| なる整数 i はちょうど 1 個である
        a_count1 = 0
        for j in range(i+1, i+n-1):
            if P[j] > P[j-1] and P[j] > P[j+1]:
                a_count1 += 1
        if a_count1 != 1:
            flag = False
            break

        # A_i−1 ​> A_i < A_i+1 ​を満たす 2 ≤ i <|A| なる整数 i はちょうど 1 個である
        a_count2 = 0
        for j in range(i+1, i+n-1):
            if P[j] < P[j-1] and P[j] < P[j+1]:
                a_count2 += 1
        if a_count2 != 1:
            flag = False
            break

        if flag:
            count += 1

print(count)
