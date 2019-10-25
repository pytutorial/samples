from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
#import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    studentNo = db.Column('student_no', db.String(20), unique=True)
    studentName = db.Column('student_name', db.String(50))

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)
    
@app.route('/create_student', methods=['GET', 'POST'])
def createStudent():
    st = Student()
    st.studentName = st.studentNo = ''    
    err = ''
    if request.method == 'POST':
        try:
            st.studentNo = request.form['studentNo']
            st.studentName = request.form['studentName']        
            db.session.add(st)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            err = str(e)
        
    return render_template('student_form.html', student=st, err=err)
    
@app.route('/update_student/<int:id>', methods=['GET', 'POST'])
def updateStudent(id):
    st = Student.query.get(id)
    err = ''
    
    if request.method == 'POST':        
        try:
            st.studentNo = request.form['studentNo']
            st.studentName = request.form['studentName']
            db.session.commit()
            return redirect('/')            
        except Exception as e:
            db.session.rollback()
            err = str(e)
            
    return render_template('student_form.html', student=st, err=err)

@app.route('/delete_student/<int:id>')
def deleteStudent(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)