# Generated by Django 5.0 on 2023-12-20 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbDemo', '0002_alter_students_contactno'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]
