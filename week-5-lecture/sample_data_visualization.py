import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\Hp\oneminuteman\coursework\Scientific-Computing\week-5-lecture\sample_data.csv")

# print data with 5 bins
print(data["temperature"].hist(bins=5))

# If your data has a lot of Nan , you can fill Nan with values
# you can replace the missing values with mean
dataNum = data.drop("category")

dataNum.fillna(dataNum.mean(), inplace=True)

# Find data that is NaN
data.isna().sum()

# Drop where its not a number
data.dropna

# Fill entry with NaN with mean
data.fillna(data["humidity"].mean(), inplace=True)
#Nan = not a number