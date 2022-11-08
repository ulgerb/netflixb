from django.shortcuts import render
from appUser.models import UserChild
from .models import *
# Create your views here.


def index(request):
    
    return render(request,'index.html')

def browserIndex(request,id,type='Full'):
    context = {}
    profil = UserChild.objects.get(id=id)
    if type=='Film':
        movie = Movie.objects.filter(video=2)
    elif type == 'Dizi':
        movie = Movie.objects.filter(video=1)
    else:
        movie = Movie.objects.all()
        movie_random = Movie.objects.all().order_by('?')[:10]
        context["movie_random"] = movie_random
    
    context.update({
        "profil":profil,
        "movie": movie,
    })
    return render(request,'browse-index.html',context)

