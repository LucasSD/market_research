from django.db import models
from django.db.models.fields import DateField


class Tile(models.Model):
    """Create a Tile model."""

    class Status(models.IntegerChoices):
        """Create a Status subclass of Tile model."""

        LIVE = 1, "Live"
        PENDING = 2, "Pending"
        ARCHIVED = 3, "Archived"

    status = models.PositiveSmallIntegerField(choices=Status.choices)
    launch_date = DateField()


class Task(models.Model):
    """Create a Task model."""

    class Type(models.IntegerChoices):
        """Create a Type subclass of Task model."""

        SURVEY = 1, "Survey"
        DISCUSSION = 2, "Discussion"
        DIARY = 3, "Diary"

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    order = models.SmallIntegerField()
    type = models.PositiveSmallIntegerField(choices=Type.choices)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, null=True)
