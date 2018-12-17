# Generated by Django 2.1.1 on 2018-12-08 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_general', '0003_votacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.TextField()),
                ('user2', models.TextField()),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('estado', models.IntegerField()),
                ('tipo', models.IntegerField()),
            ],
            options={
                'verbose_name': 'notificacion',
                'verbose_name_plural': 'notificaciones',
                'ordering': ['created'],
            },
        ),
    ]