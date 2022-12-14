# Generated by Django 4.0.6 on 2022-07-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0007_alter_news_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
