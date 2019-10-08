import pandas as pd

df_sales = pd.DataFrame({
    'id' : [1, 2, 3],
    'price' : [50000, 100000, 80000],
    'quantity' : [10, 15, 12]
})

print(df_sales)

print()
df_sales = pd.read_csv('data.csv')
print(df_sales)

df_sales.to_csv('output.csv', index=False)

print()
print('Number of rows :', len(df_sales))
print('Row 0: ', df_sales.loc[0])

print()
print('Columns : ', df_sales.columns)

print()
print('Column price : ')
print(df_sales['price'])

print()
data = df_sales.values
print('Raw data :')
print(data)