# Generated by Django 4.2.7 on 2024-09-25 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_rename_fuct_fact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fact',
            name='direction_name',
        ),
        migrations.RemoveField(
            model_name='fact',
            name='title',
        ),
    ]
