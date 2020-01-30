from app import db
from flask import Blueprint, jsonify, request
from models import Student
from serializers import StudentSerializer

service = Blueprint('service', __name__)

@service.route('/hello')
def hello():
    return jsonify({"message" : "Hello test"})
    
@service.route('/create_student', methods=['POST'])
def createStudent():
    serializer = StudentSerializer(request.json)
    if serializer.is_valid():
        student = serializer.get_object_model()
        db.session.add(student)
        db.session.commit()
        return jsonify({'success': True, 'student': student})
    else:
        return jsonify({'success': False, 'errors': serializer.errors})
    
@service.route('/update_student/<int:id>', methods=["PUT"])
def updateStudent(id):
    student = Student.query.get(id)
    serializer = StudentSerializer(request.json, student)
    if serializer.is_valid():
        student = serializer.get_object_model()
        db.session.merge(student)
        db.session.commit()
        return jsonify({'success': True, 'student': student})
    else:
        return jsonify({'success': False, 'errors': serializer.errors})

@service.route('/get_student/<int:id>')
def getStudent(id):
    student = Student.query.get(id)
    return jsonify(student)
    
@service.route('/get_all_students')
def getAllStudents():
    students = Student.query.all()
    return jsonify(students)