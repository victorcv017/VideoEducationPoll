from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('login',  auth_views.LoginView.as_view(template_name='polls/login.html'),name='login'),
    path('logout',  auth_views.LogoutView.as_view(template_name='polls/logout.html'),name='logout'),
    path('signup', views.signup, name='signup'),
    path('myvideos', login_required(views.MyVideosView.as_view()), name='myvideos'),
    path('explore/category/<int:category_id>', login_required(views.ExploreView.as_view()), name='explore'),
    path('myvideos/video/<int:video_id>', views.video, name='video'),
    path('watch/video/<int:video_id>', views.watch, name='watch'),
    path('results', views.results, name='results'),
    path('create', views.create, name='create')
]
