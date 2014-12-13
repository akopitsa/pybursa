from django.shortcuts import render, get_object_or_404
from course.models import Course


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})


def course_info(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course/course_info.html', {'course': course})
