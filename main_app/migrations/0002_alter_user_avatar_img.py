# Generated by Django 4.0.5 on 2022-06-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_img',
            field=models.CharField(max_length=500),
        ),
    ]
