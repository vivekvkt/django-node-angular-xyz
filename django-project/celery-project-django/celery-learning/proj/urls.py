# from django.urls import handler404, handler500, include, path  # noqa
from django.contrib import admin
from django.urls import path, include

#proj.urls
#app_name='demoapp'

urlpatterns = [
   # path('admin/', include(admin.site.urls)),
    #path('', include('blog.urls')),
    #path('proj/', include('demoapp.urls')),
    path('proj/', include('proj.urls')),
   
    
]
