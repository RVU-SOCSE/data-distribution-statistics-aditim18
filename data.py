import pandas as pd

df = pd.read_csv("data.csv")


print("Missing Values:\n", df.isnull())


df.fillna(df.mean(numeric_only=True), inplace=True)


df.drop_duplicates(inplace=True)

print("\nCleaned Data:\n", df)
