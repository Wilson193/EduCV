# Generated by Django 4.2.16 on 2024-11-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='clave',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]