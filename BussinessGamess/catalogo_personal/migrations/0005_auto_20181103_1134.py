# Generated by Django 2.1.1 on 2018-11-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_personal', '0004_auto_20181010_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuegos',
            name='image',
            field=models.ImageField(upload_to='image_juegos', verbose_name='Imagen'),
        ),
    ]
