# Generated by Django 4.2.1 on 2023-05-24 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_mod',
            field=models.DateTimeField(auto_now=True),
        ),
    ]