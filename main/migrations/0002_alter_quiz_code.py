# Generated by Django 5.0.2 on 2024-03-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='code',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
