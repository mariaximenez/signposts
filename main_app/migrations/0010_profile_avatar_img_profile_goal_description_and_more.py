# Generated by Django 4.0.5 on 2022-06-06 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0009_remove_user_user_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_img',
            field=models.CharField(default='1', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='goal_description',
            field=models.CharField(default='1', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
