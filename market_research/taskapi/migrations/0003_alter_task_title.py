# Generated by Django 3.2.4 on 2021-06-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskapi", "0002_task_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
