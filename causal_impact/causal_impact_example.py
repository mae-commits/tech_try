import os
import pandas as pd
from causalimpact import CausalImpact
import matplotlib.pyplot as plt

# 出力ディレクトリの作成
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory created: {output_dir}")

# データの読み込み
cigar = pd.read_csv(
    "output/cigar.txt",
    header=None,
    sep="\s+",
    names=["state", "year", "price", "pop", "pop16", "cpi", "ndi", "sales", "pimin"],
).dropna()

# スキップする州のリスト
skip_state = [3, 9, 10, 22, 21, 23, 31, 33, 48]
cigar = cigar[(~cigar["state"].isin(skip_state)) & (cigar["year"] >= 70)].reset_index(drop=True)
cigar["area"] = cigar["state"].apply(lambda x: "CA" if x == 5 else "Other states")

# カリフォルニア州のデータセットを作成
y = cigar[cigar.state == 5][["year", "sales"]].set_index("year")
y.columns = ["y"]

# ピボットテーブルの作成
X = pd.pivot_table(
    cigar[cigar.state != 5][["year", "state", "sales"]], values="sales", index="year", columns="state"
).add_prefix("X_")

# 期間の設定

pre_period = [0, 17]
post_period = [18, 22]

df_final = pd.concat([y, X], axis=1)

# トレーニングデータのフィルタリング
df_training = df_final.loc[df_final.index <= pre_period[1] + 70].dropna()

# 相関係数の計算
# threshold = 0.3
# correlation = df_training.corr()["y"]

# 相関係数が閾値を超えるカラムの識別
# columns = correlation[correlation.abs() > threshold].index
# df_final = df_final.drop(columns=["X_30"])

# 相関係数が低いカラムをドロップ
# df_final = df_final[columns]

df_final = df_final.reset_index(drop=True)
# # モデルの作成と適合
ci = CausalImpact(df_final, pre_period, post_period, model_args={"fit_method": "hmc"})

plt.figure()

print(ci.summary())
ci.plot(show=False)
# X軸の値を 70 ~ 92 に変更
plt.xticks(ticks=[0, 5, 10, 15, 20], labels=[70, 75, 80, 85, 90])

plt.savefig(os.path.join(output_dir, "causal_impact_plot_2.png"))
plt.savefig(os.path.join(output_dir, "causal_impact_plot_2.pdf"))
