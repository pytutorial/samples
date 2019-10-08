import pandas as pd

df = pd.read_csv('sales.csv')
df['date'] = df['date_order'].apply(lambda x : x[:10])
df['revenue'] = df['qty'] * df['price'] - df['promotion']

print(df.head())

#======================================== Total revenue ======================================

print('\nTotal revenue : ', df['revenue'].sum())

#======================================== Daily revenues =====================================

df_date = df.groupby('date')['revenue'].sum()
df_date = pd.DataFrame({'date' : df_date.index, 
                        'revenue' : df_date.values.astype('int')})

                        
print('\nRevenue for every day:')
print(df_date)

#======================================== Stores' revenues ===================================
df_store = df.groupby('location_id')['revenue'].sum()
df_store = pd.DataFrame({'location_id' : df_store.index, 
                         'revenue' : df_store.values.astype('int')})

df_store = df_store.sort_values(by='revenue', ascending=False)
df_store = df_store.reset_index(drop=True)
print('\nRevenue for each store :')
print(df_store)

#======================================== Average revenues for categories======================

df_categ = df.groupby('categ_id')['revenue'].mean()
df_categ = pd.DataFrame({'categ_id' : df_categ.index, 
                           'revenue' : df_categ.values.astype('int')})
                           
df_categ = df_categ.sort_values(by='revenue', ascending=False)
df_categ = df_categ.reset_index(drop=True)
print('\nAverage revenue of product in categories : ')
print(df_categ)



