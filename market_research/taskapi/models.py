from django.db import models
from django.db.models.fields import DateField


class Tile(models.Model):
    """Create a Tile model."""

    STATUS = [(1, "Live"), (2, "Pending"), (3, "Archived")]

    status = models.PositiveSmallIntegerField(choices=STATUS)

    # nullable, as might not know launch date
    launch_date = DateField(null=True)

    # need some qualitative identifier for tiles
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} -- ID: {self.id}"


class Task(models.Model):
    """Create a Task model."""

    TYPES = [
        (1, "Survey"),
        (2, "Discussion"),
        (3, "Diary"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    # nullable, as might not know order
    order = models.SmallIntegerField(null=True)

    type = models.PositiveSmallIntegerField(choices=TYPES)

    # nullable, as might not know which tile
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, null=True)

    class Meta:
        order_with_respect_to = "tile"

    def __str__(self):
        return f"{self.title} -- {self.type} -- from Tile: {self.tile.title}"
