# Generated by Django 4.2.1 on 2023-05-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagenes',
        ),
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
    ]
