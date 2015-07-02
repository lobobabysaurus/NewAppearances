from django.conf.urls import patterns, url

from services import views


urlpatterns = patterns('',
    # If no resource is specified call the services/views.py services_menu function
    url(r'^$', views.services_menu, name='services_menu'),
    # If resource is specified, call the services/views.py services function
    url(r'^(?P<category_resource>\w+)/$', views.services, name='services'),
)
