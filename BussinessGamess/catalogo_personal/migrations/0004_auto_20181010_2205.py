# Generated by Django 2.1.1 on 2018-10-11 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_personal', '0003_auto_20181008_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuegos',
            name='image',
            field=models.ImageField(height_field=600, upload_to='image_juegos', verbose_name='Imagen', width_field=480),
        ),
    ]
