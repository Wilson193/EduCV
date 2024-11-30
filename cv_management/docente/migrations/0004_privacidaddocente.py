# Generated by Django 4.2.16 on 2024-11-30 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0003_alter_docente_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacidadDocente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula_visible', models.BooleanField(default=False)),
                ('telefono_visible', models.BooleanField(default=False)),
                ('correo_visible', models.BooleanField(default=False)),
                ('categoria_visible', models.BooleanField(default=False)),
                ('contrato_visible', models.BooleanField(default=False)),
                ('fecha_contratacion_visible', models.BooleanField(default=False)),
                ('docente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='docente.docente')),
            ],
        ),
    ]
