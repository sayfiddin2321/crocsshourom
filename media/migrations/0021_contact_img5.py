# Generated by Django 5.2 on 2025-05-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_contact_img1_contact_img2_contact_img3_contact_img4'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='img5',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
