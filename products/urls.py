from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # If no resource is specified call the views.py products function
    url(r'^$', views.products, name='products'),
)
