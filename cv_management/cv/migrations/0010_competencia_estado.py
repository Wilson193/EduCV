# Generated by Django 4.2.16 on 2024-11-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_rename_competencias_competencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='competencia',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
