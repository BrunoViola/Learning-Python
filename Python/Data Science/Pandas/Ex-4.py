import pandas as pd

brics = pd.read_csv("brics.csv", index_col=0)

print(brics.loc[["BR", "CH"],["country", "capital"]])
print("\n\n")
print(brics.loc[:, ["country", "capital"]])