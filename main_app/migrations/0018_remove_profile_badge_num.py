# Generated by Django 4.0.4 on 2022-06-09 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='badge_num',
        ),
    ]
