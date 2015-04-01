from django.conf.urls import patterns, include, url
from django.contrib import admin, admindocs

urlpatterns = patterns('',
    # Forward a url with no resource specified or the home resource specified to the home application
    url(r'^(home/)?$', include('home.urls')),
     #Forward a url with the contact/ resource to the services application
    url(r'^contact/', include('contact.urls')),
    # Forward a url with the hours/ resource to the hours application
    url(r'^hours/', include('hours.urls')),
    # Forward a url with the location/ resource to the location application
    url(r'^location/', include('location.urls')),
    # Forward a url with the products/ resource to the products application
    url(r'^products/', include('products.urls')),
    # Forward a url with the services/ resource to the services application
    url(r'^services/', include('services.urls')),
    # Forward a url with admin/docs/ to the admin documentation url
    url(r'^admin/docs/', include('django.contrib.admindocs.urls')),
    # Forward a url with admin/ to the admin site url
    url(r'^admin/', include(admin.site.urls)),
)
