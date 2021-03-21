
from django.urls import path
from .views import cvpdf,resume,resumelist


urlpatterns = [ 
    path('', cvpdf ,name="cvpdf"),
    path('resume/<int:id>/', resume ,name="resume"),
    path('resumelist/', resumelist ,name="resumelist")
]