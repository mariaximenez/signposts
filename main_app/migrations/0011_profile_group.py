# Generated by Django 4.0.4 on 2022-06-06 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_profile_avatar_img_profile_goal_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='main_app.group'),
        ),
    ]