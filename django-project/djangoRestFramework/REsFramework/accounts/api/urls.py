from django.conf.urls import url,include

from rest_framework_jwt.views import refresh_jwt_token , obtain_jwt_token

urlpatterns = [
   
    url(r'^jwt-token/$', obtain_jwt_token),
    url(r'^jwt-refresh-token/$', refresh_jwt_token),
]