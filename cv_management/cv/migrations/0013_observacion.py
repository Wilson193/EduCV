# Generated by Django 4.2.16 on 2024-11-24 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coordinador_academico', '0002_coordinadoracademico_foto'),
        ('cv', '0012_alter_cv_estado_verificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('leido', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinador_academico.coordinadoracademico')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observaciones', to='cv.cv')),
            ],
        ),
    ]
