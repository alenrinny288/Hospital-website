# Generated by Django 5.0.2 on 2024-02-27 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='dep_description',
            new_name='dept_description',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='dep_name',
            new_name='dept_name',
        ),
    ]