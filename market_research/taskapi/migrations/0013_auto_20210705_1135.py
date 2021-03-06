# Generated by Django 2.2.24 on 2021-07-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskapi", "0012_auto_20210705_1126"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="order",
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Survey"), (2, "Discussion"), (3, "Diary")], default=0
            ),
            preserve_default=False,
        ),
    ]
