import pandas as pd

df = pd.read_csv("data.csv")

print("Mean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nMode:\n", df.mode())
print("\nMin:\n", df.min(numeric_only=True))
print("\nMax:\n", df.max(numeric_only=True))
print("\nVariance:\n", df.var(numeric_only=True))
print("\nStandard Deviation:\n", df.std(numeric_only=True))
