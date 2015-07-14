from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^backend/index/', 'backend.views.index'),
    url(r'^backend/add/', 'backend.views.add'),
    url(r'^backend/del/', 'backend.views.delPro'),
    url(r'^backend/portal/', 'backend.views.portal'),
=======
    url(r'^backend/login/', 'backend.views.login')
>>>>>>> b9ae8d4b0fa9e7a6ac8b5f1399fc48b8cad2f69b
)
