# Generated by Django 2.2.24 on 2021-07-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapi', '0009_auto_20210704_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Survey'), (2, 'Discussion'), (3, 'Diary')], null=True),
        ),
        migrations.AlterField(
            model_name='tile',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Live'), (2, 'Pending'), (3, 'Archived')]),
        ),
    ]