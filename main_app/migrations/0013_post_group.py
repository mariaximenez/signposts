# Generated by Django 4.0.4 on 2022-06-06 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_post_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='group', to='main_app.group'),
        ),
    ]