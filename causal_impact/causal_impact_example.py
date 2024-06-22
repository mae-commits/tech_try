import os
import pandas as pd
from causalimpact import CausalImpact
import matplotlib.pyplot as plt

# 出力ディレクトリの作成
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory created: {output_dir}")

# データの読み込み
data = pd.read_csv("https://raw.githubusercontent.com/WillianFuks/tfcausalimpact/master/tests/fixtures/arma_data.csv")[
    ["y", "X"]
]

# データのCSV保存
csv_path = os.path.join(output_dir, "sample_data.csv")
data.to_csv(csv_path, index=False)
print(f"Data saved to: {csv_path}")

# データの再読み込み（念のため）
read_data = pd.read_csv(csv_path)
print(f"Data read from: {csv_path}")

# ポストインターベンションの変更
data.iloc[70:, 0] += 5

# 期間の設定
pre_period = [0, 69]
post_period = [70, 99]

# CausalImpactの実行
ci = CausalImpact(data, pre_period, post_period)

# サマリの表示
print(ci.summary())
print(ci.summary(output="report"))

# プロットの生成と保存
plt.figure()
ci.plot()
png_path = os.path.join(output_dir, "causal_impact_plot.png")
pdf_path = os.path.join(output_dir, "causal_impact_plot.pdf")
plt.savefig(png_path)  # PNGとして保存
plt.savefig(pdf_path)  # PDFとして保存
print(f"Plot saved as PNG to: {png_path}")
print(f"Plot saved as PDF to: {pdf_path}")

# プロットの表示（オプション）
plt.show()
