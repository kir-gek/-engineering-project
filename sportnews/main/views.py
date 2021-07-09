from django.shortcuts import render
from .models import News, Category, Team, Game, Tournament, Review
from .forms import ReviewForm, ScoreFilter

# Create your views here.

def index(request):
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news})

# def about(request):
#     return HttpResponse("<h4>About</h4>") 

def review(request):
    form = ReviewForm()
    review = Review.objects.order_by('-score') #считывание отзывов

    formsort = ScoreFilter(request.GET) #форма фильтра отзывов

    #выполнение формы фильтра
    if formsort.is_valid(): 
        if formsort.cleaned_data['score_min']:
            review = review.filter(score__gte=formsort.cleaned_data['score_min'])

        if formsort.cleaned_data['score_max']:
            review = review.filter(score__lte=formsort.cleaned_data['score_max'])

    #выполнение добавления отзывов при заполнении формы
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error="Форма не валидна"
   
    return render(request, 'main/review.html', {'review': review, 'form':form, 'formsort': formsort}) 

def tournament(request):
    tournament = Tournament.objects.all()
    return render(request, 'main/tournament.html', {'tournament': tournament})