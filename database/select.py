import MySQLdb

db = MySQLdb.connect("localhost", "test", "abc@123", "testdb", charset='utf8')

cursor = db.cursor()

cursor.execute("SELECT student_no, name, gpa FROM STUDENT WHERE address=%s AND gpa >= %s", 
                                ['Hà Nội', 7.0])
                                
results = cursor.fetchall()

for st in results:
    studentNo, name, gpa = st
    print(studentNo, name, gpa)
    
db.close()