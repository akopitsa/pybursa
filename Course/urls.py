from django.conf.urls import patterns, include, url
from Course.views import course_list, course_item


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', course_list),
    url(r'^(?P<course_id>\d+)/$', course_item)
)
