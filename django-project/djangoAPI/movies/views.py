from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MovieSerialize
from .models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerialize
    
    
class ActionMovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerialize
    

class ComedyMovies(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerialize
    

class DramaMovies(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='drama')
    serializer_class = MovieSerialize
    
