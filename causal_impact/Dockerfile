# ベースイメージを指定
FROM python:3.9-slim

# 環境変数の設定（インタラクティブプロンプトを無効にするため）
ENV DEBIAN_FRONTEND=noninteractive

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && \
    apt-get install -y gcc g++ libc6-dev libatlas-base-dev pkg-config libhdf5-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# pipのアップグレード
RUN pip install --no-cache-dir --upgrade pip

# 必要なPythonライブラリをインストール
RUN pip install --no-cache-dir numpy pandas matplotlib statsmodels tfcausalimpact

# アプリケーションコードをコンテナにコピー
COPY . /app

# スクリプトを実行するためのエントリーポイントシェルスクリプトを作成
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# エントリーポイントを指定
ENTRYPOINT ["/entrypoint.sh"]
