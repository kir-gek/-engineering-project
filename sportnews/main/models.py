from django.db import models
from django.contrib.postgres.validators import (MinValueValidator, MaxValueValidator)


# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name='Название статьи', max_length=100)
    text = models.TextField(verbose_name='Текст статьи')    
  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=50)
    news = models.ManyToManyField(News, verbose_name='Новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    


class Team(models.Model):
    name = models.CharField(verbose_name='Название команды', max_length=50)
    type_of_sport = models.CharField(verbose_name='Вид спорта', max_length=50, default='')

    def __str__(self):
        return f'{self.name} - {self.type_of_sport}'

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Game(models.Model):
   

    title = models.CharField(verbose_name='Название матча', max_length=50)
    team1 = models.ForeignKey(
        Team, verbose_name='Команда 1', related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(
        Team, verbose_name='Команда 2', related_name='team2', on_delete=models.CASCADE)
    score1 = models.IntegerField(verbose_name='Счёт команды 1', default=0)
    score2 = models.IntegerField(verbose_name='Счёт команды 2', default=0)
   
    def __str__(self):
        return f"{self.title}: {self.team1} - {self.team2}"

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    

class Tournament(models.Model):
   
    title = models.CharField(verbose_name='Название турнира', max_length=50)
    description = models.TextField(verbose_name='Описание турнира')
        
    teams = models.ManyToManyField(
        Team, related_name='Tournament', verbose_name='Команды')
    games = models.ManyToManyField(
        Game, related_name='Tournament', verbose_name='Игры')
    winner = models.ForeignKey(
        Team, verbose_name="Победитель турнира", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'



class Review(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    content = models.TextField(verbose_name='Содержание')
    score = models.IntegerField(verbose_name='Оценка', validators=[MinValueValidator(1),MaxValueValidator(5)] )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
