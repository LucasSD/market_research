# Generated by Django 2.2.24 on 2021-07-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapi', '0010_auto_20210704_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]