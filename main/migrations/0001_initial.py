# Generated by Django 5.1.4 on 2025-05-10 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sana', models.DateField()),
                ('img', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discount_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='media/')),
                ('img1', models.ImageField(upload_to='media/')),
                ('img2', models.ImageField(upload_to='media/')),
                ('img3', models.ImageField(upload_to='media/')),
                ('img4', models.ImageField(upload_to='media/')),
                ('img5', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Index_Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_img', models.ImageField(upload_to='media/')),
            ],
        ),
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
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, max_length=40, null=True)),
                ('is_ordered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Small',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Xatolik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.contact')),
            ],
        ),
    ]
