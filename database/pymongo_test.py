from pymongo import MongoClient
client = MongoClient(
    '34.122.175.106', 
    username='admin', 
    password='abc@123'
)

db = client.test
productList = db.product.find()
for product in productList:
    print(product)
