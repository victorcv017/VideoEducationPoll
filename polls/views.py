from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from pprint import pprint
import urllib
import json

from .models import Video, Category, QuestionType, Question, Answer
from .forms import SignUpForm, QuestionForm, VideoForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('polls:myvideos')
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})


#---------Generic Views / login required


class MyVideosView(generic.ListView):
    template_name = 'polls/myvideos.html'

    def get_queryset(self):
        return Video.objects.filter(user=self.request.user)


class ExploreView(generic.ListView):
    template_name = 'polls/explore.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(ExploreView, self).get_context_data(**kwargs)
        context.update({
            'video_list': Video.objects.filter(category=self.kwargs['category_id'])
        })
        return context

    def get_queryset(self):
        return Category.objects.order_by('name')
    

@login_required
def create(request):
    aux = ""
    url = ""
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            aux = form.cleaned_data.get('link')
            url = urllib.parse.urlparse(aux).query
            aux = urllib.parse.parse_qs(url)
            url = aux['v'][0]
            form.save().link = url
            form.save().user = request.user
            return redirect('polls:video',video_id = form.save().id)
    else:
        form = VideoForm()
    return render(request, 'polls/create.html', {'form': form, 't' : url})

@login_required
def video(request,video_id):
    video = get_object_or_404(Video, pk=video_id)
    types = QuestionType.objects.order_by('name')
    questions = Question.objects.filter(video=video_id)
    data = ""
    text = ""
    correct = ""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        data = json.loads(request.POST.get('data'))
        correct = request.POST.get('ansradio')
        for answer in data:
            ans = Answer.objects.create(text = answer['value'], question = form.save())
            if answer['id'] == correct:
                form.save().correctAnswers = ans.id
            text = ans
            #ans.save()
        if form.is_valid():
            form.save()
        return redirect('polls:video',video_id = video_id)
    else:
        form = QuestionForm()
    return render(request, 'polls/video.html', 
    {
        'video' : video,
        'types' : types,
        'form' : form,
        'questions' : questions,
        'text' : text,
        'correct' : correct
    
    })
#/----------------------NO LOGIN REQUIRED
def results(request):
    return render(request,'polls/results.html')

def watch(request, video_id):
    data =""
    post = ""
    video = get_object_or_404(Video, pk=video_id)
    video.views = video.views + 1
    video.save()
    questions = Question.objects.filter(video=video_id)
    times = []
    maptimes = {}
    if request.method == 'POST':
        post = request.POST
        for element in request.POST:
            data = urllib.parse.parse_qs(request.POST[element])
        score = request.POST.get('score')
        answerable = request.POST.get('answerable')
        return render(request, 'polls/results.html', {
            'score': score,
            'answerable': answerable
        })

    for question in questions:
        answers = Answer.objects.filter(question = question.id)
        question.answers = answers
        question.time = question.minutes * 60 + question.seconds
        maptimes[question.time] = question.id
        times.append(question.time)
        
    return render(request , 'polls/watch.html',{
        'video' : video,
        'questions' : questions,
        'times' : times,
        'maptimes' : maptimes,
        'max' : max(times),
        'data' : data ,
        'post' : post 
    })


""" Define Antique Models

def explore(request, category_id):
    return HttpResponse("Explor page")

def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return HttpResponse("Create page")

def viewVideo(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return HttpResponse("Create page")
"""
  
