# Generated by Django 2.2.2 on 2020-03-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_auto_20200226_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cedula',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
