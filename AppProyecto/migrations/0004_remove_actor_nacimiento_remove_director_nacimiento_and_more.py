# Generated by Django 4.2.5 on 2023-09-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0003_director_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='director',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='película',
            name='director',
        ),
        migrations.RemoveField(
            model_name='película',
            name='productora',
        ),
        migrations.RemoveField(
            model_name='productora',
            name='fundacion',
        ),
        migrations.AddField(
            model_name='productora',
            name='películas',
            field=models.ManyToManyField(to='AppProyecto.película'),
        ),
    ]
