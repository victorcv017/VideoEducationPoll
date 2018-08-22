from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    name = models.CharField(max_length=200, default="Sin Titulo")
    duration = models.IntegerField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    link = models.CharField(max_length=200,blank = True, null = True)
    views = models.IntegerField(default=0)
    start = models.IntegerField(default=0)
    end = models.IntegerField()
    responses = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    videos = models.ManyToManyField(Video)
    

class QuestionType(models.Model):
    name = models.CharField(max_length=200)

class Question(models.Model):
    title = models.CharField(max_length=200)
    time = models.IntegerField()
    points = models.IntegerField(default=0)
    correctAnswers = models.CharField(max_length=200, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)


class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)



