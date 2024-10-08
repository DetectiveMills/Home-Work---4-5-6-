# Generated by Django 4.2.7 on 2024-09-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_remove_fact_description_remove_fact_direction_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logo/', verbose_name='Фото 1')),
                ('rank', models.CharField(max_length=50, verbose_name='Звание')),
                ('year', models.IntegerField(verbose_name='Год получения')),
                ('rank_association', models.CharField(max_length=50, verbose_name='Ассоциация')),
                ('place', models.CharField(max_length=50, verbose_name='Место, где получил звание')),
                ('description', models.CharField(max_length=50, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Звание',
            },
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_1',
            field=models.ImageField(upload_to='portfolio/', verbose_name='Фото 1'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_2',
            field=models.ImageField(upload_to='portfolio/', verbose_name='Фото 2'),
        ),
    ]
