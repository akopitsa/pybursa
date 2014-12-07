from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^$', include('Students.urls')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^bike/$', TemplateView.as_view(template_name='bike.html'), name='bike'),
    url(r'^students/', include('Students.urls')),
    url(r'^coaches/', include('Coaches.urls')),
    url(r'^courses/', include('Course.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
