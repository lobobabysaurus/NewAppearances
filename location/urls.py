from django.conf.urls import patterns, url

from location import views

urlpatterns = patterns('',
    # If no resource is specified call the views.py location function
    url(r'^$', views.location, name='location'),
)
