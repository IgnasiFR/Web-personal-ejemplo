# Generated by Django 4.2.4 on 2023-08-07 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_project_información_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='información',
            new_name='informacion',
        ),
    ]
