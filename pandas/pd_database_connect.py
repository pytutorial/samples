import MySQLdb
import pandas as pd

db = MySQLdb.connect("35.247.154.45", "test", "abc@123", "supermarket", charset='utf8')

sql = '''select * from sale_orderline limit 10'''

df = pd.read_sql(sql, con=db)
df.to_csv('orderline.csv', index=None)

print(df)

db.close()