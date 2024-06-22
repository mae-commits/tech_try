import os
import pandas as pd
from causalimpact import CausalImpact
import matplotlib.pyplot as plt

data = pd.read_csv(
    "https://raw.githubusercontent.com/WillianFuks/tfcausalimpact/master/tests/fixtures/comparison_data.csv",
    index_col=["DATE"],
)

# 出力ディレクトリの作成
output_dir = "output2"
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory created: {output_dir}")

csv_path = os.path.join(output_dir, "sample_data.csv")
data.to_csv(csv_path, index=False)
print(f"Data saved to: {csv_path}")

pre_period = ["2019-04-16", "2019-07-14"]
post_period = ["2019-7-15", "2019-08-01"]
ci = CausalImpact(data, pre_period, post_period, model_args={"fit_method": "hmc"})

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
