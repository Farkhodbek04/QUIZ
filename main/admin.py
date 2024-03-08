from django.contrib import admin
from . import models
from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget  # Import CKEditor5Widget from django_ckeditor_5
from .models import Quiz

class QuizAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditor5Widget(config_name='extends'))  # Use CKEditor5Widget for the 'title' field

    class Meta:
        model = Quiz
        fields = '__all__'

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm
admin.site.register(models.Question)
admin.site.register(models.Option)
admin.site.register(models.TestTaker)
admin.site.register(models.Answer)
admin.site.register(models.Result)
