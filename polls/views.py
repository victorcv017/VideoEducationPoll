from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from pprint import pprint
import json

from .models import Video, Category, QuestionType, Question, Answer
from .forms import SignUpForm, QuestionForm

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


#---------Generic Views
class MyVideosView(generic.ListView):
    template_name = 'polls/myvideos.html'

    def get_queryset(self):
        return Video.objects.order_by('-name')


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
    


def video(request,video_id):
    video = get_object_or_404(Video, pk=video_id)
    types = QuestionType.objects.order_by('name')
    questions = Question.objects.filter(video=video_id)
    data = ""
    text = ""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        data = json.loads(request.POST.get('data'))
        correct = request.POST.get('ansradio')
        for answer in data:
            ans = Answer.objects.create(text = answer['value'], question = form.save())
            text = ans
            #ans.save()
        #if form.is_valid():
            #form.save()
    else:
        form = QuestionForm()
    return render(request, 'polls/video.html', 
    {
        'video' : video,
        'types' : types,
        'form' : form,
        'questions' : questions,
        'text' : text
    
    })


class WatchVideoView(generic.DetailView):
    model = Video
    template_name = 'polls/watch.html'


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
  
