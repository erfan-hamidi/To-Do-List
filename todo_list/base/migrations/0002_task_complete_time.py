# Generated by Django 4.2.7 on 2023-12-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete_time',
            field=models.DateField(auto_now=True),
        ),
    ]
