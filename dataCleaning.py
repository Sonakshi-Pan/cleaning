import pandas as pd
import csv

df=pd.read_csv("ads.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Radius"]
del df["Distance"]

print(list(df))
df.to_csv('main.csv')