# Generated by Django 4.2.7 on 2024-09-25 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_about_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about_person',
            old_name='Nationality',
            new_name='nationality',
        ),
    ]
