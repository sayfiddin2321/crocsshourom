# Generated by Django 5.1.4 on 2025-05-27 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date',
        ),
    ]
