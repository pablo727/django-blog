# Generated by Django 5.1.7 on 2025-03-14 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='text',
            new_name='posts',
        ),
    ]
