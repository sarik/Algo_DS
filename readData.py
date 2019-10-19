import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header = None)

df[21] = df[21].astype("object")

df[21] = df[21]*2

print df[24].dtypes

#print df.describe(include="all")

#print df.info()

#path = "C:\Users\SARIK\Downloads\movies\ML\newcars.csv"

#df.to_csv("mn.csv")
