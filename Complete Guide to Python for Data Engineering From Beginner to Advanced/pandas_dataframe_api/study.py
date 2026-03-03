import pandas as pd

#df = pd.read_csv('Order.csv')

#print(df)

#print(df.to_string())


#df = pd.read_json('D:/DataEngineerStudies/file_handling/anscombe.json')

#print(df)

#df = pd.read_excel('retail_sales.xlsx')
#print(df.to_string())

# 1. Load data
df = pd.read_csv('Order.csv')

# 2. Handle Empty Cells
df.fillna(100, inplace=True) 

# 3. Remove Duplicates
df = df.drop_duplicates()

# 4. Fix Date Format
#df["order_date"] = pd.to_datetime(df["order_date"], format='%d%m%y', errors='coerce')

# 5. Print the result
print(df)

avg_sale = df.groupby('ItemType')['UnitsSold'].mean()
print(avg_sale)

df.aggregate(['sum', 'min'])

new_order_file = pd.read_csv(pd.read_csv('retail_sales.csv'))
merged_data = pd.merge(df, new_order_file, on = 'OrderID')
print(merged_data)