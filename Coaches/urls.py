from django.conf.urls import patterns, include, url
from Coaches.views import coach_item, coache_list


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', coache_list),
    url(r'^(?P<coach_id>\d+)/$', coach_item)
)
