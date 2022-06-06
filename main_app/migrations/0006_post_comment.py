# Generated by Django 4.0.5 on 2022-06-05 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('profiles', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='main_app.profile')),
            ],
            options={
                'ordering': ['text'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main_app.post')),
            ],
            options={
                'ordering': ['text'],
            },
        ),
    ]