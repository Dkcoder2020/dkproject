# Generated by Django 4.1 on 2022-08-22 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='father_name',
            new_name='father',
        ),
    ]
