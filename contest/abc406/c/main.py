N = int(input())
P = list(map(int,input().split()))

count = 0

for n in range(4, N+1):
    for i in range(N-n+1):
        A = P[i:i+n]
        
        # A_1 < A_2である 
        if A[0] >= A[1]:
            continue

        # A_i−1 ​< A_i > A_i+1 ​を満たす 2 ≤ i <|A| なる整数 i はちょうど 1 個である
        a_count1 = 0
        # A_i−1 ​> A_i < A_i+1 ​を満たす 2 ≤ i <|A| なる整数 i はちょうど 1 個である
        a_count2 = 0
        for j in range(2, n-1):
            if A[j] > A[j-1] and A[j] > A[j+1]:
                a_count1 += 1
            if A[j] < A[j-1] and A[j] < A[j+1]:
                a_count2 += 1
                
        if a_count1 != 1 or a_count2 != 1:
            continue

        count += 1

print(count)
