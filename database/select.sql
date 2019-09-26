SELECT * FROM student;
SELECT * FROM student LIMIT 1000;
SELECT * FROM student LIMIT 1,10;
SELECT * FROM student WHERE student_no='1001';
SELECT student_no, name FROM student WHERE NAME LIKE '%Văn A%';
SELECT student_no, name, gpa FROM student WHERE gpa >= 7.0 AND address = 'Hà Nội';