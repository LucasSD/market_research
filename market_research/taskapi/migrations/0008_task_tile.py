# Generated by Django 3.2.4 on 2021-07-01 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("taskapi", "0007_auto_20210701_1537"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="tile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="taskapi.tile",
            ),
        ),
    ]
