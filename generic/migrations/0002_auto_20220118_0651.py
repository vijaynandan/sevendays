# Generated by Django 3.1.14 on 2022-01-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='banner_title',
            field=models.CharField(default='Welcome to my generic page!', max_length=100),
        ),
    ]
