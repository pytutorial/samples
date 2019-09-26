import MySQLdb

db = MySQLdb.connect("localhost", "test", "abc@123", "testdb", charset='utf8')

cursor = db.cursor()

cursor.execute("DELETE FROM student WHERE id=%s", [1])
cursor.execute("DELETE FROM student WHERE student_no=%s", ['1002'])

db.commit()                                
    
db.close()