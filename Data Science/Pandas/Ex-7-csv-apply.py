import pandas as pd

brics = pd.read_csv('brics.csv', index_col=0)

brics['name_lenght']=brics['country'].apply(len)

print(brics)