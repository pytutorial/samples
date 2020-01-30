from dataclasses import dataclass
from app import db
        
@dataclass
class Student(db.Model):    
    id : int = db.Column(db.Integer, primary_key = True)
    studentNo : str = db.Column('student_no', db.String(20), constraint_not_blank=True, unique=True)
    studentName : str = db.Column('student_name', db.String(50), constraint_not_blank=True,)