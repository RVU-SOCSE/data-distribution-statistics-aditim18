import pandas as pd


data = {
    "Name": ["Aditi", "Rohan", "Meera"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print("DataFrame from Dictionary:\n", df)


df2 = pd.read_csv("data.csv")
print("\nDataFrame from CSV:\n", df2)
