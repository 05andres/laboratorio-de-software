# Generated by Django 2.1.1 on 2018-10-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telefono',
            field=models.IntegerField(verbose_name='Número de Contacto'),
        ),
    ]
