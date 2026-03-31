import pandas as pd

df = pd.read_csv("data.csv")

print("Describe:\n", df.describe())
print("\nQuantiles:\n", df.quantile([0.25, 0.5, 0.75]))
print("\nSkewness:\n", df.skew(numeric_only=True))
print("\nKurtosis:\n", df.kurt(numeric_only=True))


print("\nValue Counts:\n", df["Name"].value_counts())
