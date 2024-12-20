# Generated by Django 4.2.16 on 2024-11-09 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField()),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProduccionAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_realizacion', models.DateField()),
                ('descripcion', models.CharField(max_length=3000)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produccion_academica', to='cv.cv')),
            ],
        ),
        migrations.CreateModel(
            name='FormacionAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formacion_academica', to='cv.cv')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciaLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar_trabajo', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=3000, null=True)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencia_laboral', to='cv.cv')),
            ],
        ),
    ]
