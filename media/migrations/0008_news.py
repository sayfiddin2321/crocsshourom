# Generated by Django 5.1.4 on 2025-03-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_nike_reklama'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sana', models.DateField()),
                ('text', models.TextField()),
                ('img', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
