# Generated by Django 4.0.6 on 2022-07-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='discreption',
            new_name='description',
        ),
    ]
