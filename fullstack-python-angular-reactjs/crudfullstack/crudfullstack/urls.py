"""crudfullstack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken.views import obtain_auth_token
from crudeappangular.views import CrudeOperation,RegisterUsers,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<int:pk>/', CrudeOperation.as_view()),
    path('api/', CrudeOperation.as_view(),name='api'),
    path('api/register/', RegisterUsers.as_view(),name='register'),
    path('api/jwt-auth-login/', LoginView.as_view(),name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    path('api-jwt-auth/', obtain_jwt_token, name='api_jwt_auth'), 
   
]