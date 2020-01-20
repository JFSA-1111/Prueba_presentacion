# Generated by Django 2.2.2 on 2020-01-18 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_conectado_usuario'),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grabacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegistroLlamada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('nombre_contesta', models.CharField(max_length=45)),
                ('fecha_entrega', models.DateField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('precio_llamada', models.FloatField()),
                ('numero_contesta', models.CharField(max_length=20)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='file.Estado')),
                ('id_grabacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='file.Grabacion')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.Perfil')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
