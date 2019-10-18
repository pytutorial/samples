from django.urls import path

from app.views import *

urlpatterns = [
    path('', index, name='home'),
    path('create_student', createStudent, name='createStudent'),
    path('update_student/<int:id>', updateStudent, name='updateStudent'),
    path('delete_student<int:id>', deleteStudent, name='deleteStudent')
]