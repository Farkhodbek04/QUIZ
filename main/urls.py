from . import views

from django.urls import path


urlpatterns = [
    path('', views.index, name='index' ),
    path('create-quiz', views.create_quiz, name='create_quizes'),
    path('delete-quiz/<int:id>', views.delete_quiz, name='delete_quiz'),
    path('update-quiz', views.update_quiz, name='update_quiz')
]