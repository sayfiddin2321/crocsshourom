# Generated by Django 5.1.4 on 2025-05-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_contactsize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsize',
            name='size',
            field=models.PositiveIntegerField(),
        ),
    ]
