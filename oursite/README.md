# デプロイ手順
## git install

```
sudo yum update
sudo yum install git
git clone このレポジトリ
```

## サーバーの準備
```
cd mentaiko/oursite
bash prepare_env.sh
```
主に、次のことをやっている
- python周りのインストール
- djangoと既存のsqlite3の依存関係の整備
- uwsgiのインストール
- nginxのインストールと設定

## サーバー起動
```
bash run_server.sh
```
nginxを起動して、uwsgi経由でアプリを立ち上げている。

## 注意事項
- oursite/oursite_nginx.confのipアドレスを、立ち上げているサーバーのアドレスにする必要がある
- oursite/settings.pyのSTATIC_ROOTを有効にして、STATIC_DIRSをコメントアウトする必要がある
