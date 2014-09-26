from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from td.projects import views as projects

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', projects.home, name='home'),
    url(r'update/?$', projects.force_update, name='update')
)

