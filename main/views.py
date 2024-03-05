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

def delete_quiz(request, id):
    quizes = models.Quiz.objects.all()
    if request.method =='GET':
        quiz = models.Quiz.objects.get(id=id)
        quiz.delete()
        return redirect('index')
    return render(request, 'index.html', {'quizes':quizes})

def update_quiz(request):
    return render(request, 'quiz/update_quiz.html')

# def quiz_detail(request, id):
#     question = models.Question.objects.filter(quiz_id=id)
#     return render(request,)