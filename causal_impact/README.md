# Docker コンテナでの作業手順

## Dockerイメージのビルド

以下のコマンドを実行してDockerイメージをビルドします。

```
docker build -t causal-impact-analysis .
```

## デフォルトのスクリプトを実行

以下のコマンドでデフォルトスクリプト（`causal_impact_example.py`）を実行します。

```
docker run --rm -it -v $(pwd)/output:/app/output causal-impact-analysis
```

## 別のスクリプトを実行

以下のコマンドで任意のスクリプト（例: `causal_impact_example2.py`）を実行します。

```
docker run --rm -it -v $(pwd)/output:/app/output causal-impact-analysis causal_impact_example2.py
```

## 手動でコンテナに入る

コンテナのシェルに入ってファイル構造を確認したり、手動でスクリプトを実行するには、以下のコマンドを使用します。

```
docker run --rm -it -v $(pwd)/output:/app/output --entrypoint /bin/sh causal-impact-analysis
```

## コンテナ内でスクリプトを実行

必要であれば、手動でスクリプトを実行します。

```
python causal_impact_example2.py
```

## コンテナ内でファイル構造を確認

コンテナ内で以下のコマンドを実行して、スクリプトが存在することを確認します。

```
ls /app
```

## コンテナ内でスクリプトを実行

必要であれば、手動でスクリプトを実行します。

```
python causal_impact_example2.py
```