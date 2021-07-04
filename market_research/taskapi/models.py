from django.db import models
from django.db.models.fields import DateField


class Tile(models.Model):
    """Create a Tile model."""

    STATUS = [
    (1, 'Live'),
    (2, 'Pending'),
    (3, 'Archived')
  ]

    status = models.PositiveSmallIntegerField(choices=STATUS)
    launch_date = DateField()


class Task(models.Model):
    """Create a Task model."""

    TYPES = [
    (1, 'Survey'),
    (2, 'Discussion'),
    (3, 'Diary'),
  ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    order = models.SmallIntegerField()
    type = models.PositiveSmallIntegerField(choices=TYPES, null=True)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, null=True)
