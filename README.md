# AtCoder

AtCoderにおけるバージョン管理等を行うためのリポジトリ

Python + Docker + VSCode + WSL

## Dockerfile

・イメージの自動ビルド: Dockerfileは、アプリケーションの依存関係や設定をコードとして記述することで、手動での環境設定を自動化。これにより、環境の再現性が高まり、開発やデプロイがスムーズに。

・変更の管理: Dockerfileを使用することで、イメージの変更履歴を管理でき、どのような変更が行われたかを明確に記録できる。これにより、バージョン管理が容易になります。

`FROM` : Dockerfileの最初に必ず記述される命令。使用するベースイメージを指定。(PythonやUbuntuなど)

`RUN` : インストールなどのコマンドを実行するためのもの

`COPY` : ホストマシンのファイルやディレクトリをDockerイメージ内にコピーするための命令

`ARG` : Dockerイメージのビルド時に使用する変数を定義するための命令

## devcontainer.json

どのDockerイメージを使用するか、どの拡張機能をインストールするか、どのポートを公開するかなど、開発環境の設定を定義

Dockerfileは主にイメージをビルドするための手順を記述するものであり、必要なツールやライブラリをインストールするための命令を含む。一方、devcontainer.jsonは、VSCodeがどのようにコンテナを起動し、どの設定を適用するかを定義

## docker-compose.yml

・docker-compose.ymlでは、アプリケーションを構成する各サービス（コンテナ）を定義します。これにより、どのイメージを使用するか、どのポートを公開するか、環境変数をどう設定するかなどを明示的に記述

・YAML形式で設定を記述するため、視覚的に分かりやすく、複雑な環境でも設定を簡潔に管理

・複数のコンテナを一つのコマンドで起動・停止できるため、開発やデプロイの効率が大幅に向上。例えば、docker-compose upコマンドを実行するだけで、定義された全てのサービスを同時に起動

Dockerfileで定義したイメージを基に、devcontainer.jsonでそのイメージを使用する設定を行い、docker-compose.ymlを使用して、複数のサービスを定義し、それらを同時に起動可能

## 設定手順(初期設定)

※ 事前のインストールは既に完了済み(VSCode, Docker, WSL)

1. [参考文献](https://zenn.dev/gomatofu/articles/282adadcb5d769)を元に4つのファイル作成(Dockerfile, devcontainer.json, docker-compose.yml, requirements.txt)

2. (docker-compose.ymlのあるフォルダへ移動するために、)`cd .devcontainer`でディレクリを移動

3. Dockerコンテナをビルド
`docker-compose build`

4. Dockerコンテナを起動 `docker-compose up -d`
-dでバックグラウンドで起動させる

5. 「Dev Containers: Attach to Running Container...」を選択し、コンテナに接続する
(Remote-Containers: Open Folder in Container... とかだとうまくいかなかった)

6. 新しいウィンドウが開かれ、それでAtCoderフォルダに移動

7. 開発者ツールを使用して, Application->Cookies->"https://atcoder.jp"
からREVEL_SESSIONクッキーを取得。

8. ターミナルでacc config-dirを実行し、表示されたディレクトリ内に保存されているsesion.jsonを開く(もしくは新規作成する)。

9. REVEL_SESSION=xxxのxxxの部分に手順1で取得したREVEL_SESSIONクッキーを貼り付けて保存。
```
{
    "cookies": [
        "REVEL_SESSION=xxx"
    ]
}
```

10. `acc session`で確認, okなら問題ない

11. `oj -h` でcookie.jarファイルのパスを確認し、そのファイルのREVEL_SESSIONも先ほどと同じものを代入
```
Set-Cookie3: REVEL_SESSION="xxx"
```

12. `acc check-oj`や`oj oj login https://beta.atcoder.jp/`でログインを確認

13. /AtCoderディレクトリで、`acc config default-task-choice all`

    これにより、全問題を1回の動作で取得

14. テンプレートを設定するための準備

    ```
    cd `acc config-dir`
    mkdir python
    cd python
    touch template.json
    touch main.py
    code template.json
    ```

15. template.jsonの設定
    ```
    {
        "task":{
            "program": ["main.py"],
            "submit": "main.py"
        }
    }
    ```

16. `acc config default-template python`でデフォルトのテンプレートをpythonに変更

## もしも…

### 1. requirementsに新たなライブラリを追加したい

再度、`docker-compose build`で`docker-compose up -d`すればいい

### 2. AtCoderを一通り解き終わって終了したい

`docker-compose down`で終了(止めておくことで、裏でのリソース消費を防ぐ)

再開時は、`docker-compose up -d

### 3. acc loginでログインできない

CLIでの実行に何か制限があるらしい

以下を参考に対応できるかも

自分も同様の現象に遭遇しましたが、解決できたので手順を共有します。

1. ここにある手順を参考にしてREVEL_SESSIONクッキーを取得。
2. ターミナルでacc config-dirを実行し、表示されたディレクトリ内に保存されているsesion.jsonを開く。
3. REVEL_SESSION=xxxのxxxの部分に手順1で取得したREVEL_SESSIONクッキーを貼り付けて保存。
4. `acc session`で確認, okなら問題ない

[acc対処 1](https://kaiyou9.com/acc_and_oj_login_failed/)

[acc対処 2](https://github.com/key-moon/aclogin?tab=readme-ov-file#2-revel_session%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BC%E3%82%92%E5%8F%96%E5%BE%97)

[acc 困ってる事例](https://github.com/Tatamo/atcoder-cli/issues/66)

# 参考文献

[VSCode + DockerでAtCoderのテスト・提出ができる環境構築【Python,PyPy】](https://zenn.dev/gomatofu/articles/282adadcb5d769)

[GitHubリポジトリ](https://github.com/gomatofu/atcoder_python/)

[Dockerコンテナ接続, VSCode](https://qiita.com/75ks/items/b2961e8562c353f42d21)