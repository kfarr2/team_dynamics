from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from team_dynamics.tdapp import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include('team_dynamics.tdapp.urls')),    
)

