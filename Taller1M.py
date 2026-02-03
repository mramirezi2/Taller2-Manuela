import numpy as np
import pandas as pd 

data_frame = pd.read_csv("BikePrices.csv")
data_frame.shape
print(data_frame.head())

data_frame.isna().sum(axis=0)

indice = data_frame["Brand"]
valor = data_frame["Ex_Showroom_Price"]

ser = pd.Series(valor.values, index=indice.values)

#Modificaciones Paula
promedios = data_frame.groupby("Brand")["Ex_Showroom_Price"].mean() 
df2 = data_frame.copy() 
rellenar = data_frame["Brand"].map(promedios) 
df2["Ex_Showroom_Price"] = df2["Ex_Showroom_Price"].fillna(rellenar) 