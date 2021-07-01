from django.db import models

class Task(models.Model):
    """Create a Task model."""

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    order = models.IntegerField()
