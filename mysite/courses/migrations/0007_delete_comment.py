# Generated by Django 4.0rc1 on 2021-12-20 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_merge_0004_comment_author_0005_remove_comment_authors'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]