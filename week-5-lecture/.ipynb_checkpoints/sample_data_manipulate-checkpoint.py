import pandas as pd

data = pd.read_csv(r"C:\Users\Hp\oneminuteman\coursework\Scientific-Computing\week-5-lecture\sample_data.csv")

print(data)

data_excel = pd.read_excel(r"C:\Users\Hp\oneminuteman\coursework\Scientific-Computing\week-5-lecture\data.xlsx")

print(data_excel)

data_json = pd.read_json(r"C:\Users\Hp\oneminuteman\coursework\Scientific-Computing\week-5-lecture\data.json")

print(data_json)

