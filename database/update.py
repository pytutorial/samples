import MySQLdb

db = MySQLdb.connect("localhost", "test", "abc@123", "testdb", charset='utf8')

cursor = db.cursor()

cursor.execute("UPDATE student SET address=%s WHERE address=%s", 
                                ['TP.Hà Nội', 'Hà Nội'])

db.commit()                                
    
db.close()