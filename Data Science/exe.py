import pandas as pd


df = pd.read_csv('titanic.csv')

copy_df = df.copy()
select_df = df[["sex", "age"]]
select_df.loc[1, "age"] = 30


print(select_df)
print("\n")
print(type(select_df))






















