# Generated by Django 5.0 on 2023-12-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogDemo', '0010_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
