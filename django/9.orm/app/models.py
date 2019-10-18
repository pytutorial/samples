from django.db import models

class Student(models.Model):
   studentNo = models.CharField(db_column='student_no',  max_length=20, unique=True)                                
   studentName = models.CharField(db_column='student_name', max_length=50)                                    
