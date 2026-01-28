import numpy as np
import pandas as pd 

data_frame = pd.read_csv("BikePrices.csv")
data_frame.shape
print(data_frame.head())

data_frame.isna().sum(axis=0)

indice = df["Brand"]
valor = df["Ex_Showroom_Price"]

ser = pd.Series(valor.values, index=indice.values)