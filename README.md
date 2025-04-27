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

## 設定手順

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

7. `acc login`を実行してログイン(なおlogin failedになってそこで詰まっている)

## もしも…

### 1. requirementsに新たなライブラリを追加したい

再度、`docker-compose build`で`docker-compose up -d`すればいい

### 2. AtCoderを一通り解き終わって終了したい

`docker-compose down`で終了(止めておくことで、裏でのリソース消費を防ぐ)

再開時は、`docker-compose up -d

# 参考文献

[VSCode + DockerでAtCoderのテスト・提出ができる環境構築【Python,PyPy】](https://zenn.dev/gomatofu/articles/282adadcb5d769)

[GitHubリポジトリ](https://github.com/gomatofu/atcoder_python/)

[Dockerコンテナ接続, VSCode](https://qiita.com/75ks/items/b2961e8562c353f42d21)