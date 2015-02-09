from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #Forward a url with no resource specified to the services application
    url(r'^$', include('services.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
