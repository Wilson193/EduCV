# Generated by Django 4.2.16 on 2024-11-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docente',
            old_name='profile_picture',
            new_name='foto',
        ),
        migrations.AlterField(
            model_name='docente',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
