# Generated by Django 3.2.4 on 2021-07-01 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskapi", "0006_tile"),
    ]

    operations = [
        migrations.AddField(
            model_name="tile",
            name="launch_date",
            field=models.DateField(
                default=datetime.datetime(2021, 7, 1, 15, 37, 25, 153913)
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="task",
            name="order",
            field=models.SmallIntegerField(),
        ),
    ]
