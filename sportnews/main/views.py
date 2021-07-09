from django.shortcuts import render
from .models import News, Category, Team, Game, Tournament

# Create your views here.

def index(request):
    news = News.objects.all()
    return render(request, 'main/index.html', {'news':news})

# def about(request):
#     return HttpResponse("<h4>About</h4>") 

def about(request):
    return render(request, 'main/about.html') 