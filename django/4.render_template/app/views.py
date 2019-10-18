from django.shortcuts import render

students = [
    {'id': 1, 'studentNo' : '10001', 'name': 'Student 1'},
    {'id': 2, 'studentNo' : '10002', 'name': 'Student 2'},
    {'id': 3, 'studentNo' : '10003', 'name': 'Student 3'},
    {'id': 4, 'studentNo' : '10004', 'name': 'Student 3'}
]

def index(request):
    return render(request, 'index.html', {'students': students})