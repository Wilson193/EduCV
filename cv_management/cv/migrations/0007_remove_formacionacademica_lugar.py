# Generated by Django 4.2.16 on 2024-11-08 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_remove_formacionacademica_fecha_inicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formacionacademica',
            name='lugar',
        ),
    ]
