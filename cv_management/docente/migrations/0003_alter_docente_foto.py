# Generated by Django 4.2.16 on 2024-11-19 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0002_rename_profile_picture_docente_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_perfil/'),
        ),
    ]
