# Generated by Django 4.0.5 on 2022-06-09 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
