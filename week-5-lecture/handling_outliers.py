import matplotlib.pyplot as plt
import pandas as pd

""" Handling outliers """

data = pd.read_csv(r"C:\Users\Hp\oneminuteman\coursework\Scientific-Computing\week-5-lecture\sample_data.csv" )


""" print(data["temperature"].hist(bins=5))

# If your data has a lot of Nan , you can fill Nan with values
# you can replace the missing values with mean
dataNum = data.drop("category")

dataNum.fillna(dataNum.mean(), inplace=True)

# Find data that is NaN
data.isna().sum()

# Drop where its not a number
data.dropna """

# Fill entry with NaN with mean
data.fillna(data["humidity"].mean(), inplace=True)


# Outliers
# Identify and remove outliers using interquartile range(IQR)
q1 = data["temperature"].quantile(0.25)

q3 = data["temperature"].quantile(0.75) #in java quantile = quartile

print(q1)
print(q3)

iqr = q3 - q1
# Above the IQR by 5 is an outlier
lower_bound = iqr - 1.5

upper_bound = 1.5 + iqr

# data that has no outliers
data_no_out = data[~((data["temperature"] * (q1 - 1.5 + iqr))
                     | (data["temperature"] * (q3 + 1.5 * iqr)))]

print(data_no_out)