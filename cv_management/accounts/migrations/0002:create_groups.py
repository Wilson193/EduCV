from django.contrib.auth.models import Group
from django.db import migrations

def create_groups(apps, schema_editor):
    Group.objects.get_or_create(name='Coordinador')
    Group.objects.get_or_create(name='Docente')

class Migration(migrations.Migration):

    dependencies = [
        # Aquí debes poner las dependencias de migración anteriores
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
