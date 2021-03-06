from django.db import models
from django.db.models.fields import DateField


class Tile(models.Model):
    """Create a Tile model."""

    # need some qualitative unique identifier for tiles
    title = models.CharField(max_length=100, unique=True)

    STATUS = [(1, "Live"), (2, "Pending"), (3, "Archived")]

    status = models.PositiveSmallIntegerField(choices=STATUS)

    # nullable, as might not know launch date
    launch_date = DateField(null=True)

    def __str__(self):
        """
        Returns:
            string: title and ID of Tile.
        """
        return f"{self.title} -- ID: {self.id}"


class Task(models.Model):
    """Create a Task model."""

    KINDS = [
        (1, "Survey"),
        (2, "Discussion"),
        (3, "Diary"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    # nullable, as might not know order on creation
    order = models.SmallIntegerField(null=True)

    kind = models.PositiveSmallIntegerField(choices=KINDS)

    # nullable, as might not know which tile on creation
    tile = models.ForeignKey(
        Tile, related_name="tasks", on_delete=models.CASCADE, null=True
    )

    class Meta:
        ordering = ["tile"]

    def __str__(self):
        """
        Returns:
            string: Task title, Task kind and Tile title
        """
        return f"{self.title} -- {self.kind} -- from Tile: {self.tile.title}"
