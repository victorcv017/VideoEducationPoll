from django.db import models
from django.contrib.auth.models import User



class Video(models.Model):
    name = models.CharField(max_length=200, default="Sin Titulo")
    duration = models.IntegerField(blank= True , null= True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    link = models.CharField(max_length=200,blank = True, null = True)
    views = models.IntegerField(default=0)
    start = models.IntegerField(default=0)
    end = models.IntegerField(blank=True,null=True)
    responses = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    videos = models.ManyToManyField(Video)
    

class QuestionType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=200)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    points = models.IntegerField(default=1)
    correctAnswers = models.CharField(max_length=200,blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    


class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    #user = models.ManyToManyField(User)

    



