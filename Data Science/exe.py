import pandas as pd


df = pd.read_csv('summer.csv')

df = df["Athlete"].value_counts().index[0]


print(df)
print("\n")
print(type(df))






















