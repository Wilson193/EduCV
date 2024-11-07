# Generated by Django 4.2.16 on 2024-11-06 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docente', '0005_docente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='clave',
        ),
        migrations.RemoveField(
            model_name='docente',
            name='correo',
        ),
        migrations.AlterField(
            model_name='docente',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='docente', to=settings.AUTH_USER_MODEL),
        ),
    ]
