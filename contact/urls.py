from django.conf.urls import patterns, url

from contact import views

urlpatterns = patterns('',
    #If no resource is specified call the views.py hours function
    url(r'^$', views.contact, name='contact'),
)
