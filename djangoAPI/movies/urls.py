
from django.urls import  path,include
from rest_framework.routers import DefaultRouter


from movies import views

router = DefaultRouter()
router.register('movies',views.MovieViewSet)
router.register('action',views.ActionMovieViewSet)
router.register('comedy',views.ComedyMovies)
router.register('drama',views.DramaMovies)


app_name= 'movies'

urlpatterns = [
    path('',include(router.urls))
]