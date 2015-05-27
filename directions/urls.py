from django.conf.urls import patterns, url

from directions import views

urlpatterns = patterns('',
    # If no resource is specified call the views.py directions function
    url(r'^$', views.directions, name='directions'),
)
