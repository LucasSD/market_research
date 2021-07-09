from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers


class TileViewSet(viewsets.ModelViewSet):
    """New tiles are created from the tile list. Tiles can be read, updated and deleted by clicking
    the link corresponding to the "id" key. If a tile is deleted, all of its tasks are also deleted. 
    The tasks in each tile are listed as links assigned to the "tasks" key. These task links also 
    provide read, update and delete functionality. 
    """

    queryset = models.Tile.objects.all()
    serializer_class = serializers.TileSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """New tasks are created from the task list. Tasks can be read, updated and deleted by clicking
    the link corresponding to the "id" key. Tasks can be deleted individually. The tile which a task 
    belongs to is assigned to the "tile" key as a link. This tile link also provides read, update 
    and delete functionality.
    """

    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
