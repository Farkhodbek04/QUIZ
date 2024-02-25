from . import views

from django.urls import path


urlpatterns = [
    path('', views.index, name='index' ),
    path('create-quiz', views.create_quiz, name='create_quizes'),
]