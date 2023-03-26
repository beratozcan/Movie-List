from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.

def movie_list(request):
    movies_object = Movies.objects.all()

    movie_name = request.GET.get('movie_name')

    if movie_name != '' and movie_name is not None:
        movies_object = movies_object.filter(name__icontains=movie_name)

    paginator = Paginator(movies_object,4)
    page = request.GET.get('page')
    movies_object = paginator.get_page(page)

    
    return render(request,'newapp/movie_list.html',{'movie_objects':movies_object})