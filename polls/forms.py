from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Question, Video

QUESTION_CHOICES = (
    ('3', 'Free'),
    ('2', 'Multiple')
)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,)
    last_name = forms.CharField(
        max_length=30)
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
        labels = {
            'username' : 'Usuario',
            'first_name' : 'Nombre',
            'last_name' : 'Apellidos',
            'email' : 'Correo',
            'password1' : 'Contraseña',
            'password2' : 'Confirmar Contraseña'
        }


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'minutes','seconds', 'points' ,'type', 'video']
        labels = {
            'title': 'Pregunta',
            'minutes': 'Minuto',
            'seconds': 'Segundos',
            'points': 'Puntaje',
            'type': 'Tipo de Pregunta',
            'video': ''
        }


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'link']
        labels = {
            'name': 'Titulo del Video',
            'link' : 'Link de Youtube',
        }
