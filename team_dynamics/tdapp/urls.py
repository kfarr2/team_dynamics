from django.conf.urls import patterns, url

from . import views

#   URL path for standard view
urlpatterns = patterns('',
        url(r'^$', views.std_view, name='std_view'),
        url(r'update/?$', views.force_update, name='update')
)
