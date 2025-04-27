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

# 参考文献

[VSCode + DockerでAtCoderのテスト・提出ができる環境構築【Python,PyPy】](https://zenn.dev/gomatofu/articles/282adadcb5d769)

[GitHubリポジトリ](https://github.com/gomatofu/atcoder_python/)