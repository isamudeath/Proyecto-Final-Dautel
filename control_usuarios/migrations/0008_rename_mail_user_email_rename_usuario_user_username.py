# Generated by Django 4.2.1 on 2023-05-15 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_usuarios', '0007_alter_etiqueta_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='usuario',
            new_name='username',
        ),
    ]
