import pandas as pd

data = pd.read_csv(r"C:\Users\Hp\oneminuteman\coursework\Scientific-Computing\week-5-lecture\sample_data.csv")

print(data)

data_excel = pd.read_excel(r"C:\Users\Hp\oneminuteman\coursework\Scientific-Computing\week-5-lecture\data.xlsx")

print(data_excel)

data_json = pd.read_json(r"C:\Users\Hp\oneminuteman\coursework\Scientific-Computing\week-5-lecture\data.json")

print(data_json)

# Describe alll the fields of the data
print(data.describe(include='all'))

# Print only the top 2 entries
print(data.head(2))

# Print the bottom 2 entries
print(data.tail(2))

# sample 2 values
print(data.sample(2))

# Get info ont he dataset
print(data.info())

# get specific column(eg temperature) - returns a series
print(data["temperature"])

# get specific columns(eg temperature, humidity) - returns a series
print(data[["temperature", "humidity"]])

# Get all the columns
print(data[["temperature", "humidity", "category"]])

# Get the temparatures more than 30
print(data[data["temperature"] > 30])


# Locate specific piece of data
print(data.loc[data["category"] == 'Science', [
      "temperature", "humidity", "category"]])

# Retrieve data based on indexes
print(data.iloc[0:3, 1:3])  # Gets row 0 to 2, and columns 1 to 2

# Extract all rows where temperature >25
print(data.loc[data["temperature"] > 25])

# Exploratory data analysis
# Understangin the dataset and its characteristics

print(data.shape)

print(data.dtypes)

# Check for missing values in the datasets - sum for missing values
print(data.isnull().sum())

# Check the mean for temperatures column
print(data["temperature"].mean())

print(data["humidity"].mean())

# Calculare the mode
print(data["humidity"].mode())

# Get standard deviation
print(data["temperature"].std())

# Drop the category column so that we can calculate correlation
dataNum = data.drop("category")


# Correlation between data values
print(dataNum.corr())