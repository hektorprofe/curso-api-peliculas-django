# Generated by Django 2.1.7 on 2019-02-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pelicula_favoritos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='resumen',
            field=models.TextField(default='Lorem ipsum...'),
        ),
    ]