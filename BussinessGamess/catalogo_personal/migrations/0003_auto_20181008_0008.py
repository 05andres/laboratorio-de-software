# Generated by Django 2.1.1 on 2018-10-08 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_personal', '0002_auto_20181007_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuegos',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
