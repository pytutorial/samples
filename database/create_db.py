import MySQLdb

db = MySQLdb.connect("localhost", "test", "abc@123", "testdb", charset='utf8')

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS student")

cursor.execute('''CREATE TABLE student(
                    id BIGINT NOT NULL AUTO_INCREMENT,
                    student_no VARCHAR(10),
                    name VARCHAR(30),
                    address VARCHAR(100),
                    gpa REAL,
                    PRIMARY KEY(id)
                )DEFAULT CHARACTER SET=utf8''')

print('Create table successfully.')

db.close()