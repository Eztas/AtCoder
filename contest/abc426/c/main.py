import sys

# 再帰呼び出しの上限を、制約N, Qより大きい値に設定
# これをしないと、データのサイズが大きい場合に再帰が深くなりすぎてエラーになることがあります
sys.setrecursionlimit(2 * 10**6)

# 高速な入力を受け取るためのおまじない
input = sys.stdin.readline

def main():
    """
    メインの処理を行う関数
    """
    N, Q = map(int, input().split())

    # --- Union-Find木と関連データの初期化 ---
    # 各データは1からNまでのバージョン番号をそのままインデックスとして使えるように、
    # N+2のサイズで作成します (N+1は番兵として使います)

    # parent[i]: バージョンiが属するグループの親(代表)
    parent = list(range(N + 2))
    
    # count[i]: バージョンiが代表であるグループに属するPCの台数
    # 最初は各バージョンに1台ずつPCがあるので、全て1で初期化
    count = [1] * (N + 2)
    count[N + 1] = 0 # 番兵のPC台数は0

    # --- find操作 (経路圧縮あり) ---
    # バージョンxが最終的にどのグループに属するか(代表は何か)を返す
    def find(x):
        if parent[x] == x:
            return x
        # 親をたどる過程で、親を根に直接つなぎ替える(経路圧縮)ことで次回以降の検索を高速化
        parent[x] = find(parent[x])
        return parent[x]

    # --- ジャンプのためのデータと関数 ---
    
    # next_version[i]: バージョンi以上の、まだ処理されていない最小のバージョン
    # 最初は自分自身を指す
    next_version = list(range(N + 2))

    # find_next(x): バージョンx以上の未処理バージョンを高速に見つける
    # find関数と構造は同じで、経路圧縮も行う
    def find_next(x):
        if next_version[x] == x:
            return x
        next_version[x] = find_next(next_version[x])
        return next_version[x]

    # --- Q回のクエリ処理 ---
    for _ in range(Q):
        X, Y = map(int, input().split())

        upgraded_count = 0
        root_Y = find(Y) # アップグレード先のバージョンYが属するグループの代表

        # curは、X以下の未処理バージョンをジャンプしながら進む変数
        # まずは1以上の最初の未処理バージョンからスタート
        cur = find_next(1)

        while cur <= X:
            root_cur = find(cur)

            # curとYがまだ同じグループでなければ、統合処理を行う
            if root_cur != root_Y:
                # アップグレード台数を加算
                upgraded_count += count[root_cur]
                
                # Yのグループに統合する
                count[root_Y] += count[root_cur]
                parent[root_cur] = root_Y
            
            # バージョンcurの処理が終わったので、ジャンプ先を更新する
            # 次にcurを探しに来たときは、cur+1以降の未処理バージョンに飛ぶようにする
            next_version[cur] = find_next(cur + 1)
            
            # 次の未処理バージョンへジャンプ！
            cur = find_next(cur)

        print(upgraded_count)

if __name__ == "__main__":
    main()
    