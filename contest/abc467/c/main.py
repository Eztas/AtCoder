#したがって、私たちが調べるべきパターンは以下の 2通り
# パターンX: $A_1$ を操作しない（0回）と仮定して、後ろを辻褄が合うように決めていく。
# パターンY: $A_1$ を操作する（1回）と仮定して、後ろを辻褄が合うように決めていく。
# 体感として考えてはいたけど、これをパターン化できるという認識にまで持っていけてなかったな
# A_1だけが唯一、A_1だけを加算させても他に影響を与えずに済むという特権を持つ
# A_2以降を加算すると、他にも影響が及
# この性質でパターン分けをする発想が必要だった
# AC27の時がいけたのは、パターンXしか試していないせい

N, M = map(int,input().split()) # Mは2固定
A = list(map(int,input().split())) # 配列で返す
B = list(map(int,input().split())) # 配列で返す

counts = [0] * M

for idx, count in enumerate(counts):
    calcA = list(A) # idx=0と1で違う配列をいじらないように, あとlistにしないとオブジェクトそのものを渡す

    # 無条件で変える、別にA_2で帳尻合うし、これが過剰でもパターンXに迎合できる
    if idx == 1:
        calcA[0] += 1
        counts[idx] += 1
        
    for i in range(N-1):
        if (calcA[i]+calcA[i+1]) % M != B[i]:
            calcA[i+1] += 1
            counts[idx] += 1

print(min(counts))
    