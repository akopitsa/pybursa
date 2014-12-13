from django.contrib import admin
from course.models import Course

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'start', 'finish', 'technology', 'venue')
    search_fields = ['name']
    list_filter = ['start']
    ordering = ['start', 'finish', 'technology', 'teacher']
    radio_fields = {"technology": admin.HORIZONTAL}
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Course, CourseAdmin)
