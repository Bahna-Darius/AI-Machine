import pandas as pd


summer = pd.read_csv('summer.csv')

ps = summer["Country"]
head = ps.head()
tail = ps.tail()
slicee = ps.iloc[2]
slice_loc = summer.set_index(keys="Country")
slice_loc2 = slice_loc.loc["USA"]


print(slice_loc2)
print("\n")
print(type(ps))






















