from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Movie

def  movie_List(request):
    movie_object = Movie.objects.all()
    
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_object = movie_object.filter(name__icontains=movie_name)
        
    paginator = Paginator(movie_object,4)
    page = request.GET.get('page')
    movie_object = paginator.get_page(page)
    movie_context = {"movie":movie_object}
    return render(request,'new/movie_list.html',movie_context)
