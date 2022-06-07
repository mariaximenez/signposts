# Generated by Django 4.0.4 on 2022-06-07 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0013_post_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='author',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
