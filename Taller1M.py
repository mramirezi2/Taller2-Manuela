import numpy as np
import pandas as pd 

data_frame = pd.read_csv("BikePrices.csv")
data_frame.shape
print(data_frame.head())

data_frame.isna().sum(axis=0)