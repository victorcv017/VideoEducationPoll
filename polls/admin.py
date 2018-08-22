from django.contrib import admin

from .models import Video, Category, Question, QuestionType, Answer

admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionType)