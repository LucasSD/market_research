from django.contrib import admin

from .models import Tile, Task


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    """Encapsulate all admin options and functionality for Tile model."""

    list_display = ("id", "title", "launch_date", "status")
    list_filter = ("launch_date", "status")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Encapsulate all admin options and functionality for Task model."""

    list_display = ("id", "title", "description", "order", "kind", "tile")
    list_filter = ("kind", "tile")
