# Generated by Django 5.0.2 on 2024-03-08 10:41

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_quiz_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Title'),
        ),
    ]
