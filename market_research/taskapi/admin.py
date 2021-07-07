
from django.contrib import admin

from .models import Tile, Task


@admin.register(Tile)
class LegalDocAdmin(admin.ModelAdmin):
    """Encapsulate all admin options and functionality for Tile model."""

    list_display = ("id", "launch_date", "status")
    list_filter = ("launch_date", "status")


@admin.register(Task)
class TagAdmin(admin.ModelAdmin):
    """Encapsulate all admin options and functionality for Task model."""
    list_display = ("description", "order", "type", "tile")
    list_filter = ("type", "tile")

