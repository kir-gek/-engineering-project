from main.models import Category, Game, News, Team, Tournament
from django.contrib import admin
from .models import News, Category, Team, Game, Tournament, Review
# Register your models here.

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Tournament)
admin.site.register(Review)