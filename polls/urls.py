from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('login',  auth_views.LoginView.as_view(template_name='polls/login.html'),name='login'),
    path('logout',  auth_views.LogoutView.as_view(template_name='polls/logout.html'),name='logout'),
    path('signup', views.signup, name='signup'),
    path('myvideos', views.MyVideosView.as_view(), name='myvideos'),
    path('explore/category/<int:category_id>', views.ExploreView.as_view(), name='explore'),
    path('myvideos/video/<int:video_id>', views.video, name='video'),
    path('watch/video/<int:pk>', views.WatchVideoView.as_view(), name='watch')
]
