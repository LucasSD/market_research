# Generated by Django 2.2.24 on 2021-07-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapi', '0008_task_tile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Live'), (2, 'Pending'), (3, 'Archived')]),
        ),
    ]