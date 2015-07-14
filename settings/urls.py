from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^backend/index/', 'backend.views.index'),
    url(r'^backend/add/', 'backend.views.add'),
    url(r'^backend/del/', 'backend.views.delPro'),
    url(r'^backend/portal/', 'backend.views.portal'),
)
