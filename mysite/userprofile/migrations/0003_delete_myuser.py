# Generated by Django 4.0rc1 on 2021-12-22 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_myuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
