# Generated by Django 3.2.4 on 2021-06-18 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserLoginInfoAndCRUD', '0003_alter_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='img',
        ),
    ]
