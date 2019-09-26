import MySQLdb

db = MySQLdb.connect("localhost", "test", "abc@123", "testdb" )

print('Connected to database')
