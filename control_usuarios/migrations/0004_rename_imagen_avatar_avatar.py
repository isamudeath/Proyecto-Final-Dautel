# Generated by Django 4.2.1 on 2023-05-22 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_usuarios', '0003_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='avatar',
        ),
    ]
