import MySQLdb

db = MySQLdb.connect("localhost", "test", "abc@123", "testdb", charset='utf8')

cursor = db.cursor()

class Student:
    def __init__(self, studentNo, name, address, gpa):
        self.studentNo = studentNo
        self.name = name
        self.address = address
        self.gpa = gpa
        
    def __repr__(self):
        return self.name

students = [
                Student('1001', 'Nguyễn Văn A', 'Hà Nội', 7.5),
                Student('1002', 'Nguyễn Văn B', 'TP.HCM', 8.0)
           ]

try:
    for st in students:
        cursor.execute('INSERT INTO student(student_no, name, address, gpa) VALUE(%s,%s,%s,%s)',
                            (st.studentNo, st.name, st.address, st.gpa))
                            
        print('Successfully created student : ', st)
                                        
                                        
    db.commit()
except Exception as e:
    print(str(e))
    db.rollback()

db.close()