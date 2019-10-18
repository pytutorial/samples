from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, "index.html", {'students': students})

def createStudent(request):
    st = Student()
    st.studentName = st.studentNo = ''
    err = ''

    if request.method == 'POST':
        try:
            st.studentNo = request.POST['studentNo']
            st.studentName = request.POST['studentName']
            st.save()
            return redirect('home')
        except Exception as e:
            err = str(e)

    return render(request, 'student_form.html', {'student': st, 'err': err})

def updateStudent(request, id):
    st = Student.objects.get(pk=id)
    err = ''

    if request.method == 'POST':
        try:
            st.studentNo = request.POST['studentNo']
            st.studentName = request.POST['studentName']
            st.save()
            return redirect('home')
        except Exception as e:
            err = str(e)
    
    return render(request, 'student_form.html', {'student': st, 'err': err})

def deleteStudent(request, id):
    st = Student.objects.get(pk=id)
    st.delete()
    return redirect('home')