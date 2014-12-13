from django.contrib import admin
from student.models import Student, Dossier





class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'package')
    search_fields = ['name']
    list_filter = ['package']
    ordering = ['name', 'package']
    radio_fields = {"package": admin.HORIZONTAL}
    prepopulated_fields = {"slug": ("name", )}


class DossierAdmin(admin.ModelAdmin):
    filter_horizontal = ['unliked_courses']
    radio_fields = {"favourite_color": admin.HORIZONTAL}



admin.site.register(Student, StudentAdmin)
admin.site.register(Dossier, DossierAdmin)
