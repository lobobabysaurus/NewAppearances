from django.conf.urls import patterns, url

from hours import views

urlpatterns = patterns('',
    #If no resource is specified call the views.py hours function
    url(r'^$', views.hours, name='hours'),
)
