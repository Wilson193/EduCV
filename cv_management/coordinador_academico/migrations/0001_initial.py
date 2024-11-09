# Generated by Django 4.2.16 on 2024-11-09 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordinadorAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.BigIntegerField(unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('num_telefono', models.BigIntegerField(blank=True, null=True)),
                ('universidad', models.CharField(blank=True, max_length=100, null=True)),
                ('cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('clave', models.CharField(blank=True, max_length=20, null=True)),
                ('dependencia', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono_oficina', models.BigIntegerField(blank=True, null=True)),
                ('oficina', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coordinador_academico', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
