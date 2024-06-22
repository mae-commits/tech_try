#!/bin/sh

# デフォルトのスクリプトを設定
DEFAULT_SCRIPT="causal_impact_example.py"

# 実行するスクリプトが指定されているか確認
if [ -z "$1" ]; then
  SCRIPT=$DEFAULT_SCRIPT
else
  SCRIPT=$1
fi

# 指定されたスクリプトを実行
exec python $SCRIPT
