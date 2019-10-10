import pandas as pd

df = pd.read_csv('sales.csv')
df['date'] = df['date_order'].apply(lambda x : x[:10])
df['revenue'] = df['qty'] * df['price'] - df['promotion']

print(df.head())

#======================================== Total revenue ======================================

print('\nTotal revenue : ', df['revenue'].sum())

#======================================== Daily revenues =====================================

df_date = df.groupby('date')['revenue'].sum()
                        
print('\nRevenue for every day:')
print(df_date)

#======================================== Stores' revenues ===================================
df_store = df.groupby('location_id')['revenue'].sum()
df_store = df_store.sort_values(ascending=False)
print('\nRevenue for each store :')
print(df_store)

