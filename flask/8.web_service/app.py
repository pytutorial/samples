from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

students = [
    {'id': 1, 'studentNo' : '10001', 'name': 'Student 1'},
    {'id': 2, 'studentNo' : '10002', 'name': 'Student 2'},
    {'id': 3, 'studentNo' : '10003', 'name': 'Student 3'},
    {'id': 4, 'studentNo' : '10004', 'name': 'Student 3'}
]

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/get_students')
def getStudents():
    return jsonify(students)
    
app.run(debug=True)    