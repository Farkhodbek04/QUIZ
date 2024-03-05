import random
import string

from django.contrib.auth.models import User

from django.db import models
from django.core.exceptions import ValidationError

class Quiz(models.Model): 
    """ This is table of quiz. """
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, blank=True, unique=True)

    @property
    def quiz_questions(self):
        num_of_questions = Question.objects.filter(quiz = self).count()
        return num_of_questions
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.sample(string.ascii_letters+string.digits, 20))
            super(Quiz, self).save(*args, **kwargs)


class Question(models.Model):
    """ This class is for table of question. """
    question = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    @property
    def correct_answer(self):
        try:
            correct_option = Option.objects.get(question=self, is_true=True)
            return True
        except Option.DoesNotExist:
            return False
        

class Option(models.Model):
    """ This is for table of option. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.TextField()
    is_true = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        option = Option.objects.filter(question=self.question, is_true=True)
        if option.count() > 1 and self.is_true:
            return ValidationError("To'g'ri javob 1 tadan ko'p bo'lishi mumkin emas!")
        elif not self.is_true:
            return ValidationError("To'g'ri javobni ko'rsating!")
        super(Option, self).save(*args, **kwargs)


class TestTaker(models.Model):
    """ The class is table of Test taker. """
    full_name = models.CharField(max_length=255)
    tel_num = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class Answer(models.Model):
    """ Table of Answers """
    test_taker = models.ForeignKey(TestTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Option, on_delete=models.CASCADE)

    @property
    def is_correct(self):
        try:
            correct_option = Option.objects.get(question=self.question, is_true=True)
            if correct_option == self.answer:
                return True  
        except Option.DoesNotExist:
            return False
        

class Result(models.Model):
    """ Table of Results """
    test_taker = models.ForeignKey(TestTaker, on_delete=models.CASCADE)

    @property
    def correct_answers(self):
        result = Answer.objects.filter(test_taker=self.test_taker, is_correct=True).count()
        return result

    @property
    def incorrect_answers(self):
        result = Answer.objects.filter(test_taker=self.test_taker, is_correct=False).count()
        return result
    
    @property
    def all_questions(self):
        return self.incorrect_answers+self.correct_answers

    @property
    def percentage(self):
        result = self.correct_answers/self.all_questions*100
        return result



