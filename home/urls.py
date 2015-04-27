__author__ = 'prs'

from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    # If no resource is specified call the views.py home function
    url(r'^$', views.home, name='home'),
)
