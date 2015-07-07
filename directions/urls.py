from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # If no resource is specified call the views.py directions function
    url(r'^$', views.directions, name='directions'),
    # When save is the resource attempt to save the entered location
    url(r'^save', views.save_location, name='save')
)
