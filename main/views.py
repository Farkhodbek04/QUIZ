from . import models

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_ckeditor_5.widgets import CKEditor5Widget 

def index(request):
    if request.method == 'GET':
        quizes = models.Quiz.objects.all()
        # questions = models.Question.objects.filter(quiz=quizes)
    return render(request, 'index.html', {'quizes':quizes})

# @login_required
def create_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Get the title from the POST data
        if title:  # Check if the title is not empty
            author = request.user  # Get the current user as the author
            models.Quiz.objects.create(title=title, author=author)  # Create a new Quiz instance with the title and author
            return redirect('index')  # Redirect to the index page after successful creation
    return render(request, 'quiz/create_quiz.html')  # Render the create_quiz.html template


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