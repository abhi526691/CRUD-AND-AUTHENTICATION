# Generated by Django 3.2.4 on 2021-06-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserLoginInfoAndCRUD', '0004_remove_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Img',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
