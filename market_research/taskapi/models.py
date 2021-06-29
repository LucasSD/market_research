from django.db import models

class Task(models.Model):
    """Create a Task model."""

    title = models.CharField(max_length=100)
