from . import models

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'GET':
        quizes = models.Quiz.objects.all()
        # questions = models.Question.objects.filter(quiz=quizes)
    return render(request, 'index.html', {'quizes':quizes})

# @login_required
def create_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.user
        print(title)
        if title and author:
            models.Quiz.objects.create(title=title, author=author)
            return redirect('index')
        # if title:
        # return render(request, 'quiz/create_quiz.html')
    return render(request, 'quiz/create_quiz.html')
