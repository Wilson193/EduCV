# Generated by Django 4.2.16 on 2024-11-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_rename_fecha_realizacion_produccionacademica_fecha_publicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencialaboral',
            name='certificado',
            field=models.FileField(blank=True, null=True, upload_to='certificados/'),
        ),
        migrations.AddField(
            model_name='experiencialaboral',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='formacionacademica',
            name='certificado',
            field=models.FileField(blank=True, null=True, upload_to='certificados/'),
        ),
        migrations.AddField(
            model_name='formacionacademica',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='produccionacademica',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cv',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]