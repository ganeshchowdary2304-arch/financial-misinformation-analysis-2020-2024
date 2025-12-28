import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/financial_misinformation_2020_2024_full_dataset.csv")

yearly = df.groupby("year").size()
yearly.plot(kind="line", title="Yearly Misinformation Trends")
plt.savefig("docs/figures/yearly_trend.png")

city_counts = df["city"].value_counts()
city_counts.plot(kind="bar", title="Events by City")
plt.savefig("docs/figures/city_distribution.png")

narr_counts = df["narrative_type"].value_counts()
narr_counts.plot(kind="bar", title="Narrative Types")
plt.savefig("docs/figures/narrative_distribution.png")

df["tone_score"].plot(kind="hist", bins=20, title="Tone Distribution")
plt.savefig("docs/figures/tone_distribution.png")

df["mentions"].plot(kind="hist", bins=15, title="Amplification Distribution")
plt.savefig("docs/figures/amplification_distribution.png")

print("Analysis visuals saved successfully.")
