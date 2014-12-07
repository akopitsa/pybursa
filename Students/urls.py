from django.conf.urls import patterns, include, url
from Students.views import students_list, students_item


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', students_list),
    url(r'^(?P<student_id>\d+)/$', students_item)
)
