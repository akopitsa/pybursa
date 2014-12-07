from django.shortcuts import render
from Course.models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses': courses})


def course_item(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course/item.html', {'course': course})
