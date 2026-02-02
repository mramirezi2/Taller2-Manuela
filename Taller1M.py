import numpy as np
import pandas as pd 

data_frame = pd.read_csv("BikePrices.csv")
data_frame.shape
print(data_frame.head())

data_frame.isna().sum(axis=0)

indice = df["Brand"]
valor = df["Ex_Showroom_Price"]

ser = pd.Series(valor.values, index=indice.values)

#Modificaciones Paula
promedios = df.groupby("Brand")["Ex_Showroom_Price"].mean() 
df2 = df.copy() 
rellenar = df["Brand"].map(promedios) 
df2["Ex_Showroom_Price"] = df2["Ex_Showroom_Price"].fillna(rellenar) 