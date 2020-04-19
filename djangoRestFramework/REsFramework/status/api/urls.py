from django.conf.urls import url


from .views import (
    #StatusListSerachAPIView,
    GenericStatusLisAPIView,
    #GenericStatusCreateAPIView,
    #GenericStatusDetailAPIView,
    # GenericStatusUpdateAPIView,
    # GenericStatusDeleteAPIView,
    StatusAPIDetailView,
    
)

urlpatterns = [
    #url(r'^$',StatusListSerachAPIView.as_view()),
    # url(r'^create/$',StatusCreateAPIview.as_view()),
    # url(r'^(?P<id>.*)/$',StatusDetailAPIview.as_view()),
    # url(r'^(?P<id>.*)/update/$',StatusUpdateAPIview.as_view()),
    # url(r'^(?P<id>.*)/delete/$',StatusDeleteAPIview.as_view()),
    #generic class 
    url(r'^$',GenericStatusLisAPIView.as_view()),
    #url(r'^create/$',GenericStatusCreateAPIView.as_view()),
    #url(r'^(?P<pk>\d+)/$',GenericStatusDetailAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/update/$',GenericStatusUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$',GenericStatusDeleteAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
    
]