# Generated by Django 4.0rc1 on 2021-12-17 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_comment_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='authors',
        ),
    ]
