# Generated by Django 5.0.6 on 2024-06-19 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafioadl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtarea',
            old_name='tarea_id',
            new_name='tarea',
        ),
    ]
