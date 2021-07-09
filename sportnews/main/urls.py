from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('review', views.review),
   path('tournament', views.tournament)
]
