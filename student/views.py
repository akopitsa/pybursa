from django.shortcuts import render
from student.models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})


def student_info(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student/student_info.html', {'student': student})
