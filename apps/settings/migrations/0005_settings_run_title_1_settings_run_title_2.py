# Generated by Django 4.2.7 on 2024-09-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_contact_settings_image4'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='run_title_1',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='run_title_2',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
