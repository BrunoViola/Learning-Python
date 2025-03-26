import pandas as pd

brics = pd.read_csv("brics.csv", index_col=0)

for value in brics:
   print(value)

print("\n\n")

for lab, row in brics.iterrows():
   print(lab)
   print(row)

print("\n\n")

for lab, row in brics.iterrows():
   print(f'{lab}: {row["country"]}')