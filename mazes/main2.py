import pandas as pd

path = "./csv/maze1.csv"

df = pd.read_csv(path, header=None)
df[df.isna()] = " "
df.to_csv(path, header=None, index=None)