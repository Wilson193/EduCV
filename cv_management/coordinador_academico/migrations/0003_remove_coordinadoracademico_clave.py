# Generated by Django 4.2.16 on 2024-12-02 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador_academico', '0002_coordinadoracademico_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinadoracademico',
            name='clave',
        ),
    ]