# Generated by Django 4.2.16 on 2024-11-23 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_cv_github_cv_linkedin_cv_x'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Competencias',
            new_name='Competencia',
        ),
    ]
