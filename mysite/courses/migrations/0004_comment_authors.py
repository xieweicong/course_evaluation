# Generated by Django 4.0rc1 on 2021-12-17 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('courses', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='authors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userprofile.profile'),
        ),
    ]
