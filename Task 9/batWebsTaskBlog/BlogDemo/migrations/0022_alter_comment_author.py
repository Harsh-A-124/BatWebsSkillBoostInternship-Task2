# Generated by Django 5.0 on 2024-01-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogDemo', '0021_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]